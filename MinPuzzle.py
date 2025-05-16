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
    # can use a priority queue here
    dist = [[float('infinity')] * n for _ in range(m)]
    dist[0][0] = 0

