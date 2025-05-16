# Name: Honggwan Shin
# Date: May 14, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Graph Algorithms 1

def minEffort(Graph, puzzle):
    # the goal is to reach the bottom-right cell '[m-1][n-1]' with minimal effort.

    m, n = len(puzzle), len(puzzle[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # up, down, left ,right

    # Step 1: Initialize distances and visited nodes
    dist = [[float('infinite')] * n for _ in range(m)]
    dist[0][0] = 0
    # starting node

    unvisited = set(Graph.nodes)

    while unvisited:
        # loop to find the node with the shortest distance
        minimum_distance = float('infinite')
        currentNode = None
        for node in unvisited:
            row, column = node
            if dist[row][column] < minimum_distance:
                minimum_distance = dist[row][column]
                currentNode = node

        if currentNode is None:
            break
            # when no node is left
        unvisited.remove(currentNode)
        row, column = currentNode




