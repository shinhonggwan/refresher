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

    selected = [False] * number_of_nodes
    # track selected nodes
    tour = [0]
    current = 0
    selected[current] = True

    while len(tour) < number_of_nodes:
        nearest = None
        minimum_distance = float('inf')

        for i in range(number_of_nodes):
            # finding the nearrest unvisited neighbor
            if G[current][i] > 0 and not selected[i]:
                # iteration, find the unvisited
                if G[current][i] < minimum_distance:
                    minimum_distance = G[current][i]
                    nearest = i

        if nearest is None:
            # if there is no more nodes to visit, then stop
            break

        tour.append(nearest)
        selected[nearest] = True
        current = nearest

    tour.append(0)
    return tour


