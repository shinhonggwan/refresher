# Name: Honggwan Shin
# Date: May 22, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Greedy Technique & Graph Algorithms Part-2

def connect_bridges(G):
    # This is modified from the concept shown through The Exploration 7.3 Minimum Spanning Tree - Prim's Algorithm work/exmple.py
    # This produces a list of tubles of two islands and the cost of the bridge between them

    number_of_islands = len(G)
    # total number of islands
    distance = []
    previous_node = []

    for i in range(number_of_islands):
        # initialize distance and previou node arrays
        distance.append(float('inf'))
        previous_node.append(None)

    visited = set()
    # track visited nodes
    MST = []
    # store MST edges

    distance[0] = 0
    # starting from island 0

    while len(visited) < number_of_islands:
        # Step 1: Find the unvisited node with the smallest distance until visiting all islands
        currentNode = None
        for v in range(number_of_islands):
            if v not in visited and (currentNode is None or distance[v] < distance[currentNode]):
                currentNode = v

        if currentNode is None:
            # if there is no unvisited node remaining
            break

        visited.add(currentNode)

        # Add the edge to MST (except for the starting node)
        if previous_node[currentNode] is not None:
            MST.append((previous_node[currentNode], currentNode, distance[currentNode]))

        # Step 2: Update distances for neighbors
        for neighbor in range(number_of_islands):
            # iteration through all possible neighboring islands
            edge_weight = G[currentNode][neighbor]
            # retrieve weight of cost of the edge
            if neighbor not in visited and edge_weight != 0 and edge_weight < distance[neighbor]:
                # if neighbor not in visited and there is no actual bridge between currentnode and neighbor and the currentnode cost is lower than the previous
                distance[neighbor] = edge_weight
                previous_node[neighbor] = currentNode

    return MST


