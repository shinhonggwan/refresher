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

def dna_match_bottomup(DNA1, DNA2):
    # this will take some time, but using iteration
    length_dna1 = len(DNA1)
    length_dna2 = len(DNA2)

    # Creating a 2D memo table as shown from the Exploration 4.2 work/example.py
    cache = [[0] * (length_dna2 + 1) for x in range(length_dna1 +1) ]

    # inserting strings into the table created above row by row from left to right
    for i in range(length_dna1-1, -1, -1):
        # from length_dna1 - 1 to 0
        for j in range(length_dna2-1, -1, -1):
            # from length_dna 2 to 0
            if DNA1[i] == DNA2[j]:
                # if DNA[i] character and DNA[j] character match
                cache[i][j] = 1 + cache[i + 1][j + 1]
            else:
                # if they don't
                cache[i][j] = max(cache[i + 1][j], cache[i][j +1])

    return cache[0][0]

#print(dna_match_bottomup("TAGTTCCGTCAAA", "GTGTTCCCGTCAAA"))