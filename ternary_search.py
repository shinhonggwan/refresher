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
        middle_index_1 = ( (right - left) + left ) // 3
        middle_index_2 = ( right - (right - left) ) // 3

    return search_function()



