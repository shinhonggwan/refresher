# Name: Honggwan Shin
# Date: May 14, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Graph Algorithms 1

def minEffort(puzzle):
    # the goal is to reach the bottom-right cell '[m-1][n-1]' with minimal effort.

    m, n = len(puzzle), len(puzzle[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # up, down, left ,right

    # Step 1: Initialize distances and visited nodes
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0
    # starting node

    unvisited = {(i, j) for i in range(m) for j in range(n)}

    while unvisited:
        # loop to find the node with the shortest distance
        minimum_distance = float('inf')
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

        for row_difference, column_difference in directions:
            new_row, new_column = row + row_difference, column + column_difference
            if 0 <= new_row + m and 0 <= new_column < n and (new_row, new_column) in unvisited:
                effort = abs(puzzle[row][column] - puzzle[new_row][new_column])
                maxEffort = max(dist[row][column], effort)
                if maxEffort < dist[new_row][new_column]:
                    dist[new_row][new_column] = maxEffort

        return dist[m-1][n-1]


puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print(minEffort(puzzle))
