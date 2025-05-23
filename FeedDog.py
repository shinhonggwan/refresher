# Name: Honggwan Shin
# Date: May 22, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Greedy Technique & Graph Algorithms Part-2

def feedDog(hunger_level, biscuit_size):
    # a dog feeding function that tells how many dogs can satisfy with biscuits
    result = []

    hunger = 0
    biscuit = 0

    n = len(hunger_level)
    m = len(biscuit_size)



    while hunger < n and biscuit < m:
        if