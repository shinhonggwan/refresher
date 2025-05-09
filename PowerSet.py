# Name: Honggwan Shin
# Date: May 7, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Backtracking

from copy import deepcopy

def powerset(input_set):

    def permutations_backtracking(starting_index, subset, output):
        output.append(subset[:])

        for i in range(starting_index, len(input_set)):
            for i in range(starting_index, len(input_set)):
