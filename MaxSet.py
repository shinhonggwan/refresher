# Name: Honggwan Shin
# Date: May 1, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment 4: Dynamic Programming

def max_independent_set(nums):

    if all(x < 0 for x in nums) or not nums:
        # returns nothing if the numbers from the list are either all negative or there is no value
        return []

    length_num = len(nums)

    cache = [0] * (length_num + 1)
    # initializing the base case

    for i in range(1, length_num +1 ):
        current = nums[i -1]
        # jumps back to the previous value if the value is valid
        take = current + (cache[i - 2] if i > 1 else 0)
        jump = cache[i - 1]
        cache[i] = max(take, jump)

    new_list = []
    x = length_num
    # start from the end
    while x >= 1:
        if x == 1:
            # if only one value left
            if cache[x] > 0:
                # add the value to the list
                new_list.append(nums[0])
            break
        if cache[x] == cache[x - 1]:
            # if the current value equals the value before then move to the previous index
            x -= 1
        else:
            # Anything else are considered valid thus add
            new_list.append(nums[x -1])
            # and then move to the previous one from the previous one
            x -= 2

    return new_list[::-1]
            # reverse the order since the values are from the end





