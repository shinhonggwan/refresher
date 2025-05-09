# Name: Honggwan Shin
# Date: May 8, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Backtracking



def permutations_backtracker(starting_index, combination, remainder_sum, unique_numbers, counter, results):
    if remainder_sum == 0:
        # if the remaining sum is 0, the combination is valid thus add it to the result
        results.append(combination[:])
        return
    if remainder_sum < 0:
        # if the remaining sum is below 0, then stop
        return



def amount(nums_list, target_sum):
    counter = {}
    # a dictionary that counts how many times
    for number in nums_list:
        if number in counter:
            counter[number] += 1
        else:
            counter[number] = 1

    unique_numbers = sorted(counter.keys())
    results = []

    permutations_backtracker(0, [], target_sum, unique_numbers, counter, results)
    return results

# nums_list = [11, 1, 3, 2, 6, 1, 5]
# target_sum = 8
# print(amount(nums_list, target_sum))
# wtf...