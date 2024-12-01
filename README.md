# Assignment_3

This assignment is meant to capture the methods needed to implement the distance vector routing algorithm. An algorithm that involves sending data between connected routers in order to find an ideal path between the routers.

## Dependencies

- Python v3.11.5

## Installation

This broject can be installed by pip installing fromt he root of the folder. For example

```bash
pip install .
```

### Running the DVR algorithm

In order to run the DVR algorithm we will essentially leverage the network.txt file that we have from the assignment. It can be run like so:

```bash
python dvr/run.py
```

This runs the dvr algorithm on the base network file, it can also be run on a different network file as well like so

```bash
python dvr/run.py --network-file networks/network_2.txt
```

### Interpreting Results

When the dvr algorithm has finished running we can see a log that is produced that looks like so:

```bash
[33;20m2024-12-01 14:03:19,569 [INFO] Beginning run of DVR with ./networks/network_1.txt[0m
[33;20m2024-12-01 14:03:19,575 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,575 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,575 [INFO] Round 0: Node 0[0m
[33;20m2024-12-01 14:03:19,575 [INFO] Receiving DV from Node 1[0m
[33;20m2024-12-01 14:03:19,575 [INFO] Receiving DV from Node 4[0m
[33;20m2024-12-01 14:03:19,576 [INFO] Current DV Matrix: [[ 0.  2. inf inf  1.]
 [ 2.  0.  5. inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,577 [INFO] Last DV Matrix [[ 0.  2. inf inf  1.]
 [ 2.  0.  5. inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,577 [INFO] Updated[0m
[33;20m2024-12-01 14:03:19,577 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,577 [INFO] Round 0: Node 1[0m
[33;20m2024-12-01 14:03:19,577 [INFO] Receiving DV from Node 0[0m
[33;20m2024-12-01 14:03:19,577 [INFO] Receiving DV from Node 2[0m
[33;20m2024-12-01 14:03:19,577 [INFO] Current DV Matrix: [[ 0.  2. inf inf  1.]
 [ 2.  0.  5. inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,578 [INFO] Last DV Matrix [[ 0.  2. inf inf  1.]
 [ 2.  0.  5. inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,578 [INFO] Updated[0m
[33;20m2024-12-01 14:03:19,578 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,578 [INFO] Round 0: Node 2[0m
[33;20m2024-12-01 14:03:19,578 [INFO] Receiving DV from Node 1[0m
[33;20m2024-12-01 14:03:19,578 [INFO] Receiving DV from Node 3[0m
[33;20m2024-12-01 14:03:19,578 [INFO] Current DV Matrix: [[inf inf inf inf inf]
 [ 2.  0.  5. inf inf]
 [inf  5.  0.  4. inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,578 [INFO] Last DV Matrix [[inf inf inf inf inf]
 [ 2.  0.  5. inf inf]
 [inf  5.  0.  4. inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,578 [INFO] Updated[0m
[33;20m2024-12-01 14:03:19,578 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,578 [INFO] Round 0: Node 3[0m
[33;20m2024-12-01 14:03:19,578 [INFO] Receiving DV from Node 2[0m
[33;20m2024-12-01 14:03:19,579 [INFO] Receiving DV from Node 4[0m
[33;20m2024-12-01 14:03:19,579 [INFO] Current DV Matrix: [[inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf  5.  0.  4. inf]
 [inf inf  4.  0.  1.]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,579 [INFO] Last DV Matrix [[inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf  5.  0.  4. inf]
 [inf inf  4.  0.  1.]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,579 [INFO] Updated[0m
[33;20m2024-12-01 14:03:19,579 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,579 [INFO] Round 0: Node 4[0m
[33;20m2024-12-01 14:03:19,579 [INFO] Receiving DV from Node 0[0m
[33;20m2024-12-01 14:03:19,579 [INFO] Receiving DV from Node 3[0m
[33;20m2024-12-01 14:03:19,580 [INFO] Current DV Matrix: [[ 0.  2. inf inf  1.]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [ 1. inf inf  1.  0.]][0m
[33;20m2024-12-01 14:03:19,580 [INFO] Last DV Matrix [[inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [ 1. inf inf  1.  0.]][0m
[33;20m2024-12-01 14:03:19,580 [INFO] Updated[0m
[33;20m2024-12-01 14:03:19,580 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,581 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,581 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,581 [INFO] Round 1: Node 0[0m
[33;20m2024-12-01 14:03:19,581 [INFO] Receiving DV from Node 1[0m
[33;20m2024-12-01 14:03:19,581 [INFO] Receiving DV from Node 4[0m
[33;20m2024-12-01 14:03:19,581 [INFO] Current DV Matrix: [[ 0.  2. inf inf  1.]
 [ 2.  0.  5. inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [ 1. inf inf  1.  0.]][0m
[33;20m2024-12-01 14:03:19,582 [INFO] Last DV Matrix [[ 0.  2. inf inf  1.]
 [ 2.  0.  5. inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [ 1. inf inf  1.  0.]][0m
[33;20m2024-12-01 14:03:19,582 [INFO] Not Updated[0m
[33;20m2024-12-01 14:03:19,582 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,582 [INFO] Round 1: Node 1[0m
[33;20m2024-12-01 14:03:19,582 [INFO] Receiving DV from Node 0[0m
[33;20m2024-12-01 14:03:19,582 [INFO] Receiving DV from Node 2[0m
[33;20m2024-12-01 14:03:19,582 [INFO] Current DV Matrix: [[ 0.  2. inf inf  1.]
 [ 2.  0.  5. inf inf]
 [inf  5.  0.  4. inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,582 [INFO] Last DV Matrix [[ 0.  2. inf inf  1.]
 [ 2.  0.  5. inf inf]
 [inf  5.  0.  4. inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,582 [INFO] Not Updated[0m
[33;20m2024-12-01 14:03:19,582 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,582 [INFO] Round 1: Node 2[0m
[33;20m2024-12-01 14:03:19,582 [INFO] Receiving DV from Node 1[0m
[33;20m2024-12-01 14:03:19,583 [INFO] Receiving DV from Node 3[0m
[33;20m2024-12-01 14:03:19,583 [INFO] Current DV Matrix: [[inf inf inf inf inf]
 [ 2.  0.  5. inf inf]
 [inf  5.  0.  4. inf]
 [inf inf  4.  0.  1.]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,583 [INFO] Last DV Matrix [[inf inf inf inf inf]
 [ 2.  0.  5. inf inf]
 [inf  5.  0.  4. inf]
 [inf inf  4.  0.  1.]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,583 [INFO] Not Updated[0m
[33;20m2024-12-01 14:03:19,583 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,583 [INFO] Round 1: Node 3[0m
[33;20m2024-12-01 14:03:19,583 [INFO] Receiving DV from Node 2[0m
[33;20m2024-12-01 14:03:19,583 [INFO] Receiving DV from Node 4[0m
[33;20m2024-12-01 14:03:19,584 [INFO] Current DV Matrix: [[inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf  5.  0.  4. inf]
 [inf inf  4.  0.  1.]
 [ 1. inf inf  1.  0.]][0m
[33;20m2024-12-01 14:03:19,584 [INFO] Last DV Matrix [[inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf  5.  0.  4. inf]
 [inf inf  4.  0.  1.]
 [ 1. inf inf  1.  0.]][0m
[33;20m2024-12-01 14:03:19,584 [INFO] Not Updated[0m
[33;20m2024-12-01 14:03:19,584 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,584 [INFO] Round 1: Node 4[0m
[33;20m2024-12-01 14:03:19,584 [INFO] Receiving DV from Node 0[0m
[33;20m2024-12-01 14:03:19,584 [INFO] Receiving DV from Node 3[0m
[33;20m2024-12-01 14:03:19,584 [INFO] Current DV Matrix: [[ 0.  2. inf inf  1.]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf inf  4.  0.  1.]
 [ 1. inf inf  1.  0.]][0m
[33;20m2024-12-01 14:03:19,584 [INFO] Last DV Matrix [[ 0.  2. inf inf  1.]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf inf  4.  0.  1.]
 [ 1. inf inf  1.  0.]][0m
[33;20m2024-12-01 14:03:19,585 [INFO] Not Updated[0m
[33;20m2024-12-01 14:03:19,585 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,585 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,585 [INFO] Final Output:[0m
[33;20m2024-12-01 14:03:19,585 [INFO] Node 0 DV = [[ 0.  2. inf inf  1.]
 [ 2.  0.  5. inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [ 1. inf inf  1.  0.]][0m
[33;20m2024-12-01 14:03:19,585 [INFO] Node 1 DV = [[ 0.  2. inf inf  1.]
 [ 2.  0.  5. inf inf]
 [inf  5.  0.  4. inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,585 [INFO] Node 2 DV = [[inf inf inf inf inf]
 [ 2.  0.  5. inf inf]
 [inf  5.  0.  4. inf]
 [inf inf  4.  0.  1.]
 [inf inf inf inf inf]][0m
[33;20m2024-12-01 14:03:19,585 [INFO] Node 3 DV = [[inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf  5.  0.  4. inf]
 [inf inf  4.  0.  1.]
 [ 1. inf inf  1.  0.]][0m
[33;20m2024-12-01 14:03:19,585 [INFO] Node 4 DV = [[ 0.  2. inf inf  1.]
 [inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf inf  4.  0.  1.]
 [ 1. inf inf  1.  0.]][0m
[33;20m2024-12-01 14:03:19,585 [INFO] Number of rounds till convergence = 2[0m
[33;20m2024-12-01 14:03:19,585 [INFO] ----------------------[0m
[33;20m2024-12-01 14:03:19,586 [INFO] finished[0m
```

This essentially covers the number of rounds till convergence. Updates on the matrices changing, and information about distance vectors swapping.
