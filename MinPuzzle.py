# Name: Honggwan Shin
# Date: May 14, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Graph Algorithms 1

def minEffort(puzzle):
    # the goal is to reach the bottom-right cell '[m-1][n-1]' with minimal effort.
    # The below code is modified version of the concept shown at Exploration 6.3 Dijkstra's algorithm work/example.py

    m, n = len(puzzle), len(puzzle[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # up, down, left ,right

    # Step 1: Initialize distances and visited nodes
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0
    # starting node

    unvisited = {(i, j) for i in range(m) for j in range(n)}

    while unvisited:
        # loop to find the node with the minimum distance
        min_distance = float('inf')
        currentNode = None
        for node in unvisited:
            # go through all unvisited nodes
            row, column = node
            if dist[row][column] < min_distance:
                # find the cell that requires minimum effort
                min_distance = dist[row][column]
                currentNode = node

        if currentNode is None:
            break
            # when no node is left, break
        unvisited.remove(currentNode)
        # currentNode has been visited thus remove it from unvisited
        row, column = currentNode

        for row_difference, column_difference in directions:
            # go through the neighbos of currentNode
            new_row, new_column = row + row_difference, column + column_difference
            # get the neighbor cell row and the neighbor cell column
            if 0 <= new_row < m and 0 <= new_column < n and (new_row, new_column) in unvisited:
                # if the new cell row and the new cell column within puzzle within the puzzel limits
                # and unvisitied
                effort = abs(puzzle[row][column] - puzzle[new_row][new_column])
                # get the difference in height between the current and the neighbor
                maxEffort = max(dist[row][column], effort)
                # maxEffort = worst effort from start to the neighbor
                if maxEffort < dist[new_row][new_column]:
                    # if there is smaller effort, then replace
                    dist[new_row][new_column] = maxEffort

    return dist[m-1][n-1]