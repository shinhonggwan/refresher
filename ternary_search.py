# Name: Honggwan Shin
# Date: April 24, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment 3 Correctness of Algorithms and Divide & Conquer


def ternary_search(input_list, target):

    def search_function(left, right):
        if left > right:
            # This is the base case
            return None

        # Thie effectivly breaks the array into three parts
        middle_index_1 = left + (right - left)  // 3
        middle_index_2 = right - (right - left)  // 3

        # This checks if the target is at the either of middle points
        if input_list[middle_index_1] == target:
            # this returns 1-indexed position
            return middle_index_1 + 1
        if input_list[middle_index_2] == target:
            return middle_index_2 + 1

        # This group of recursive searches decides which third part
        if target < input_list[middle_index_1]:
            # seraching the left third
            return search_function(left, middle_index_1 - 1)
        if target > input_list[middle_index_2]:
            # searching the right third
            return search_function(middle_index_2 + 1, right)
            # searching the middle third
        else:
            return search_function(middle_index_1 + 1, middle_index_2 - 1)

    return search_function(0, len(input_list) - 1)


#print(ternary_search([10, 20, 30, 40, 50], 40))



