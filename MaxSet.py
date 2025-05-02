# Name: Honggwan Shin
# Date: May 1, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment 4: Dynamic Programming

def max_independent_set(nums):

    if all(x < 0 for x in nums) or not nums:
        # returns empty if the numbers from the list are all negative or no num in the list
        return []

    length_num = len(nums)

    cache = [(0, []) for x in range(length_num)]
    # initialize base case and other subproblem values to 0

    if nums[0] > 0:
        # this is the base case for the first value
        cache[0] = (nums[0], nums[0])
    else:
        cache[0] = (0, [])


