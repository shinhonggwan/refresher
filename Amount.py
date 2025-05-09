# Name: Honggwan Shin
# Date: May 8, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Backtracking

# the below code is modified from the Exploration 5.3 work/example.py
def permutations_backtracker(starting_index, combination, remainder_sum, unique_numbers, counter, results):
    if remainder_sum == 0:
        # base case
        # if the remaining sum is 0, the combination is valid thus copy, add it to the result
        results.append(combination.copy())
        return
    if remainder_sum < 0:
        # if the remaining sum is below 0, then stop exploring
        return

    for i in range(starting_index, len(unique_numbers)):
        # iterate from start till the end
        number = unique_numbers[i]
        if counter[number] > 0:
            # if the number hasn't been used, then pick this number, add it to combination, and minus one to the oucnter
            combination.append(number)
            counter[number] -= 1

            permutations_backtracker(i, combination, remainder_sum - number, unique_numbers, counter, results)
            # recursion. only use the smae number if there is other possible options
            combination.pop()
            # get rid of the last number and try another combination
            counter[number] += 1

def amount(nums_list, target_sum):
    counter = {}
    # a dictionary that counts how many times each number take place
    for number in nums_list:
        if number in counter:
            counter[number] += 1
        else:
            counter[number] = 1

    unique_numbers = sorted(counter.keys())
    # sorts list of unique numbers and no same combination
    result = []

    permutations_backtracker(0, [], target_sum, unique_numbers, counter, result)
    # backtracker starting from 0
    return result

nums_list = [11, 1, 3, 2, 6, 1, 5]
target_sum = 8
print(amount(nums_list, target_sum))
