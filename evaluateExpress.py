# Name: Honggwan Shin
# Date: April 17, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment 2 Recursion and Recurrence Relations

def evaluateString(input):
    if "+" not in input:
        return input
    else:
        first, last = input.split("+", 1)
        return input(first) + evaluateString(last)

print(evaluateString("2+3+4"))