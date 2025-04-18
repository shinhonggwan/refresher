# Name: Honggwan Shin
# Date: April 17, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment 2 Recursion and Recurrence Relations

def evaluateString(input):
    "calculates a simple string of integers combined with + operator"
    # if + not found, then returns the input
    if "+" not in input:
        return int(input)
    else:
        first, last = input.split("+", 1)
        return int(first) + evaluateString(last)

# print(evaluateString("2+3+4"))