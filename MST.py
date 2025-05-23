# Name: Honggwan Shin
# Date: May 22, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Greedy Technique & Graph Algorithms Part-2

def connect_bridges(G):
    # This took The Exploration 7.3 Minimum Spanning Tree - Prim's Algorithm work/exmple.py as an example.
    # This produces a list of tubles of two islands and the cost of the bridge between them

    number_of_islands = len(G)
    distance = [float('inf')] * number_of_islands
    previous_node = [None] * number_of_islands

    visited = set()
    MST = []

    distance[0] = 0

    while len(visited) < :
        currentNode = None
        for v in range(len(G)):
            if v