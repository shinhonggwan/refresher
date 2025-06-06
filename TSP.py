# Name: Honggwan Shin
# Date: June 5, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Heuristic Algorithms

# The below function took note of the pseudocode as well as the
# work/solution.py from Exploration 9.2 - Heuristic Algorithms for NP-Hard Problems

def solve_tsp(G):
    # traveling salesman problem
    # returning a list of indices indicating the path taken

    solution = [0]
    number_of_nodes = len(G)
    visited = [False] * number_of_nodes
    path = [0]
    visited[0] = True
    current_node = 0




