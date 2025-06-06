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

        for i in range(number_of_nodes):
            if G[unvisited][i] < key[i] and G[unvisited][i] > 0 and not selected[i]:
                key[i] = G[unvisited][i]
                parent[i] = unvisited

    for i in range(1, n):
        # make the MST as an adjacency list
        if parent[i] != -1:
            MST[parent[i]].append(i)
            MST[i].append(parent[i])

    def dfs(unvisited, visited_nodes, tour):
        # performing DFS traversal on the MST
        visited_nodes[unvisited] = True
        tour.append(unvisited)
        for i in MST[unvisited]:
            if not visited_nodes[i]:
                dfs(i, visited_nodes, tour)

    visited_nodes = [False] * number_of_nodes
    tour = []
    dfs(0, visited_nodes, tour)
    tour.append(0)

    return tour

G = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0],
]

print(solve_tsp(G))

