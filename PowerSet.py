# Name: Honggwan Shin
# Date: May 7, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Backtracking

from copy import deepcopy

def permutations_backtracking(starting_index, combination, output, input_set):
    output.append(combination[:])
    # Adds the combination set as a copy to the output

    for i in range(starting_index, len(input_set)):
        # iteratating
        combination.append(input_set[i])
        permutations_backtracking(i + 1, combination, output, input_set)
        # backtrack
        combination.pop()


def powerset(input_set):
    output = []
    # list storage for all combination sets
    permutations_backtracking(0, [], output, input_set)
    return output

print(powerset([1,2,3]))
