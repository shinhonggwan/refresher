# Name: Honggwan Shin
# Date: June 5, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Heuristic Algorithms

# The below function took note of the Traveling Salesman Problem section
# and the Minimum Spanning Tree-based Heuristic section
# from the Exploration 9.3 - Heuristic Algorithms for Traveling Salesman Problem

def solve_tsp(G):
    # traveling salesman problem (TSP)
    # Using MST-based heuristic
    # returning a list of node indices indicating the TSP tour path

    number_of_nodes = len(G)
    #total number of nodes in the graph

    MST = [[] for _ in range(number_of_nodes)]
    # MST as an adjacency list
    selected = [False] * number_of_nodes
    # track selected nodes
    key = [float('inf')] * number_of_nodes
    # store edge that connects
    parent = [-1] * number_of_nodes
    # store parent node in the MST
    key[0] = 0
    # start from node 0

    for _ in range(number_of_nodes):
        # Finding the univisited node with lowest key value using Prim's Algorithm
        unvisited = -1
        minimum_key = float('inf')
        for i in range(number_of_nodes):
            # iteration, find the unvisiteed with minimum key
            if not selected[i] and key[i] < minimum_key:
                minimum_key = key[i]
                unvisited = i

        if unvisited == -1:
            # if there is no more nodes to visit, then stop
            break

        selected[unvisited] = True
        # record selected node for the MST

        for i in range(number_of_nodes):
            # updating key and parent for adjacent nodes
            if G[unvisited][i] < key[i] and G[unvisited][i] > 0 and not selected[i]:
                # if node i hasn't been selected and weidhts is greater than 0
                key[i] = G[unvisited][i]
                parent[i] = unvisited
                # parent of i i = current node in MST

    for i in range(1, number_of_nodes):
        # convert the MST array to as an adjacency list
        unvisited = parent[i]
        if unvisited != -1:
            MST[unvisited].append(i)
            # append i as a neighbor of its parent
            MST[i].append(unvisited)
            # append parent as a neighbor of i

    def DFS(unvisited, visited_nodes, tour):
        # creating TSP path by performing DFS traversal on the MST
        visited_nodes[unvisited] = True
        tour.append(unvisited)
        # append univisited node to tour path
        for i in MST[unvisited]:
            # for loop to visit all unvisited neighbors
            if not visited_nodes[i]:
                DFS(i, visited_nodes, tour)
                # recursion

    visited_nodes = [False] * number_of_nodes
    # record visited nodes while DFS operation
    tour = []
    # TSP Tour result
    DFS(0, visited_nodes, tour)
    # DFS operation from node 0
    tour.append(0)
    # go back to 0 starting node

    return tour


