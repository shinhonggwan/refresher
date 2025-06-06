# Name: Honggwan Shin
# Date: June 5, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Heuristic Algorithms

# The below function took note of the Traveling Salesman Problem section
# and the Minimum Spanning Tree-based Heuristic section
# from the Exploration 9.3 - Heuristic Algorithms for Traveling Salesman Problem

def solve_tsp(G):
    # traveling salesman problem
    # returning a list of indices indicating the path taken

    number_of_nodes = len(G)

    MST = [[] for _ in range(number_of_nodes)]
    selected = [False] * number_of_nodes
    key = [float('inf')] * number_of_nodes
    parent = [-1] * number_of_nodes
    key[0] = 0

    for _ in range(n):
        unvisited = -1
        minimum_key = float('inf')
        for i in range(number_of_nodes):
            if not selected[i] and key[i] < minimum_key:
                minimum_key = key[i]
                unvisited = i

        if unvisited == -1:
            break

        selected[unvisited] = True


