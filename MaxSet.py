# Name: Honggwan Shin
# Date: May 1, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment 4: Dynamic Programming

def max_independent_set(nums):

    if all(x < 0 for x in nums) or not nums:
        # returns empty if the numbers from the list are all negative or no num in the list
        return []

    length_num = len(nums)

    cache = [0] * (length_num + 1)
    # initializing base.

    for i in range(1, length_num +1 ):
        current = nums[i -1]
        # jump back to the previous one if the value will be used
        take = current + (cache[i - 2] if i > 1 else 0)
        jump = cache[i - 1]
        cache[i] = max(take, jump)



