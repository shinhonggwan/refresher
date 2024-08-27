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

def rev_string_list(list):
    new_list = []
    for i in list:
        new_list.append(i[::-1])
    return new_list

#word = "hello"
#print(word[::-1])

print(rev_string_list(list2))