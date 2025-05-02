# Name: Honggwan Shin
# Date: May 1, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment 4: Dynamic Programming

def dna_match_topdown(DNA1, DNA2):

    def subsequence(x, y):
        # a recursive function to calculate the best continuous length
        if x == len(DNA1) or y == len(DNA2):
            # base case
            return 0


