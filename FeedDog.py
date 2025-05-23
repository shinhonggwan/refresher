# Name: Honggwan Shin
# Date: May 22, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Greedy Technique & Graph Algorithms Part-2


def feedDog(hunger_level, biscuit_size):
    # a dog feeding function that tells how many dogs can satisfy with biscuits
    result = []

    n = len(hunger_level)
    m = len(biscuit_size)

    hungry = 0
    biscuit = 0

    sorted_hunger_level = hunger_level.sort()
    sorted_biscuit_size = biscuit_size.sort()

    while hungry < n and biscuit < m:
        if sorted_biscuit_size[biscuit] >= sorted_hunger_level[hungry]:

            hungry += 1
        biscuit += 1

    return hungry



print(feedDog([1, 2, 3], [1, 1]))