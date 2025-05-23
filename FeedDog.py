# Name: Honggwan Shin
# Date: May 22, 2025 Oregon Time
# Course: CS 325
# Assignment: Assignment: Greedy Technique & Graph Algorithms Part-2


def feedDog(hunger_level, biscuit_size):
    # a dog feeding function that tells how many dogs can satisfy with biscuits

    # Need to sort the hunger level of dogs and biscuit sizes from small to big to satisfy many hungry dogs possible
    sorted_hunger_level = sorted(hunger_level)
    sorted_biscuit_size = sorted(biscuit_size)

    # indexing for hungry dogs and biscuit sizes
    hungry = 0
    biscuit = 0

    while hungry < len(hunger_level) and biscuit < len(biscuit_size):
        if sorted_biscuit_size[biscuit] >= sorted_hunger_level[hungry]:
            # if the current biscuit can satisfy the current hungry dog
            hungry += 1
            # feed the dog and move to the next one
        biscuit += 1
        # move the biscuit index to the next

    return hungry
