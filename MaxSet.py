# Name: Honggwan Shin
# Date: May 1, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment 4: Dynamic Programming

def max_independent_set(nums):

    if all(x < 0 for x in nums) or not nums:
        # returns empty if the numbers from the list are all negative or no num in the list
        return []

    length_num = len(nums)


