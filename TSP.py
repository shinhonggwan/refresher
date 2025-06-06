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

    while len(path) < number_of_nodes:

