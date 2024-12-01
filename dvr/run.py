import typer
from pathlib import Path
import logging
import numpy as np
import threading
import socket
import math
import io
import struct

# initialize our logger
logger = logging.getLogger()

###############################################################
################### Main Running Methods ######################
###############################################################

def run(network_file: str = './networks/network_1.txt'):
	"""
	The purpose of this method is to serve as the running method for our assignment.

	:param network_file: is the file that 
	"""
	
	# open log file and start logging
	logging.basicConfig(level=logging.INFO, 
					format="\x1b[33;20m%(asctime)s [%(levelname)s] %(message)s\x1b[0m",
					handlers=[
						logging.StreamHandler(),
						logging.FileHandler("log.txt")
			   		])
	
    # Start by logging initial parameters
	logger.info(f'Beginning run of DVR with {network_file}')
	
    # Read in the Adjacency File
	network_string = Path(network_file).read_text()

    # Create our network 
	network = create_network(network_string)

	# Run our Distance Vector Routing
	dvr(network)

	# Log that this has finished
	logger.info('finished')

def create_network(network_string: str) -> dict:
	"""
	this creates a dictionary of all the nodes in graph based on the network string.
	"""
	network ={}
	nodes = network_string.split('\n')
	for idx, n in enumerate(nodes):
		weights = n.split(' ')
		network[idx] = Node(idx, weights, idx+10000)
		
	return network

def dvr(graph: dict):
	"""
	This method takes in the network graph and implements the logic for 
	"""
	# For our order
	stop_condition = False

	# test index
	idx = 0

	# While we haven't broken our start condition
	while not stop_condition:
		# keep count of the number of nodes that are changing
		change = False
		logger.info(f'----------------------')
		# For every node in our graph
		for idx2, val in enumerate(graph.values()):	
			logger.info(f'----------------------')
			# Log the current round and the node
			logger.info(f'Round {idx}: Node {val.id}')

			# Send our current Distance Vector Matrix to each of the neighbors
			for neighbor in val.neighbors:
				# Log which neighbor we are sending data to
				logger.info(f'Receiving DV from Node {neighbor}')
				# Keep track of our current node
				n_node = graph[neighbor]
				# swap the dv from the neighbors
				n_node.socket.sendto(struct.pack('!H', n_node.id) + n_node.current_rt.tobytes(), ('localhost', val.port))

			# Log our current Distance Vector Matrix
			logger.info(f"Current DV Matrix: {graph[idx2].current_rt}")
			# Log our last Distance Vector Matrix
			logger.info(f"Last DV Matrix {graph[idx2].last_rt}")
			
			# Check if the graph has been updated
			if (graph[idx2].current_rt == graph[idx2].last_rt).all():
				logger.info('Not Updated')
			else:
				logger.info('Updated')
				change = True

		
		logger.info(f'----------------------')
		# Update our overall idx for breaking
		idx+=1

		# If our stop conditions are met then break it
		if idx > 10 or not change:
			stop_condition = True

	# Print our final network appearance
	print_network(graph)

	logger.info(f'Number of rounds till convergence = {idx}')
	logger.info(f'----------------------')

	# Close our our graph now that we are done.
	close_network(graph)

def close_network(graph: dict):
	"""
	The purpose of this method is to clean up all of the listening threads for the
	network and to close out the program. When called this sends a stop command to
	every node in the network.
	"""
	cleanup = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	cleanup.bind(('localhost', 15000))
	for node in graph.values():
		cleanup.sendto(b'stop', ('localhost', node.port))
	cleanup.close()

def print_network(graph: dict):
	"""
	The purpose of this method is to print out the final outputs of the nodes distance
	vectors.
	"""
	logger.info(f'----------------------')
	logger.info('Final Output:')
	for node in graph.values():
		logger.info(f'Node {node.id} DV = {node.current_rt}')

def bellman_ford(curr_dv, new_rt, neighbor):
	"""
	The purpose of this method is to perform the bellman ford calculation on the matrix
	to calculate new minimum distances.
	"""
	for i in range(curr_dv.shape[0]):  # for each source node
		for j in range(curr_dv.shape[1]):  # for each destination node
			# If the current known distance is greater than the distance via the neighbor,
			# update it.
			if curr_dv[i, j] > curr_dv[i, neighbor] + new_rt[neighbor, j]:
				logger.info(f"Updating distance from Node {i} to Node {j} via Neighbor {neighbor}")
				curr_dv[i, j] = curr_dv[i, neighbor] + new_rt[neighbor, j]



	
		

###############################################################
####################### Node Class ############################
###############################################################

class Node:
	"""
	The purpose of the node class is to represent the information attached to each node in our network.
	This consists of the current node ID and the 
	"""
	def __init__(self, id, dist_vec, port):
		# initialize the node
		self.id = id
		# initialize the routing table for the node
		self.current_rt = self.initialize_routing_table(dist_vec)
		# initialize the last routing table for the node
		self.last_rt = self.initialize_routing_table(dist_vec)
		# initialize the neighbors for the node
		self.neighbors = self.initialize_neighbors(dist_vec)
		# initialize the socket for the node.
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		# bind the socket to the localhost
		self.socket.bind(('localhost', port))
		# specify port as an attribute
		self.port = port
		# specify receiving thread
		self.recv_thread = threading.Thread(target=self.receive_data, args=(self.socket,))
		# start the receiving thread
		self.recv_thread.start()

	def initialize_routing_table(self, weights):
		"""
		The purpose of this method is to initialize a routing table based on the distance vector
		for the node
		"""
		rt = np.full((len(weights), len(weights)), np.inf)
		for col_idx, weight in enumerate(weights):
			value = int(weight)
			if col_idx == self.id:
				value = 0
			elif value == 0:
				value = np.inf
			rt[self.id, col_idx ] = value
		return rt
	
	def initialize_neighbors(self, weights):
		"""
		The purpose of this method is to determine which nodes are connected in order to know where
		to send the current nodes routing table to.
		"""
		neighbors = []
		for col_idx, weight in enumerate(weights):
			value = int(weight)
			if col_idx == self.id:
				continue
			elif value == 0:
				continue
			else:
				neighbors.append(col_idx)
		return neighbors

	def receive_data(self, socket):
		"""
		This method serves as the parsing for the data on each node.
		"""
		while True:
			received_data, recv_addr = socket.recvfrom(1472)
			# if we receive the stop signal then clean up the threads
			if received_data == b'stop':
				return
			else:
				# backup our data
				self.last_rt = self.current_rt.copy()
				# Open the data we are receiving
				file = io.BytesIO(received_data)
				# Capture the id of the neighbor sending the data
				recv_id = struct.unpack('!H', file.read(2))[0]
				# Capture the DV table we are receiving
				data = np.frombuffer(file.read(len(received_data) - 2))
				# Get the dimension of the matrix
				N = int(math.sqrt(data.shape[0]))
				# Reformat so we have the matrix we have received.
				recv_dv = data.reshape(N, N)
				# Swap the DV row with the router that is included
				self.current_rt[recv_id, :] = recv_dv[recv_id, :]
				# Now run through our bellman equation to update our current DV
				bellman_ford(self.current_rt, recv_dv, recv_id)
				





		
	

# Run the server
if __name__ == '__main__':
	typer.run(run)