# honggwan shin

def every_other(list):
    return list[::2]

list1 = ["parsley", "sage", "rosemary", "thyme"]
print(every_other(list1))

def array_sum(list):
    # we need them in one word and count
    counter = 0
    for i in list:
        counter += len(i)
    return counter

list2 = ["Wayne", "Katie","Daryl", "Don"]

print(array_sum(list2))