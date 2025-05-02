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

        if DNA1[x] == DNA2[y]:
            # if the characters line up together, include it and move to the ext one
            return 1 + subsequence(x + 1, y + 1)

        else:
            # if they dont, then skip a character either in DNA1 or DNA2
            return max(subsequence(x + 1, y), subsequence(x, y +1))

    return subsequence(0, 0)
    # recursion from the start of both characters

# print(dna_match_topdown("TAGTTCCGTCAAA", "GTGTTCCCGTCAAA"))

def dna_match_topdown(DNA1, DNA2):

    return None