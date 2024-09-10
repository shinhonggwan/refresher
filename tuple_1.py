some_tuple = (1, 2, 3)
num_1, num_2, num_3 = some_tuple
print(num_1)

print("---------")

def insert_front(list, something):
    # list.append(something)
    # need to insert something to the front of the list
    new_answer = [something] + list
    return new_answer

print(insert_front([9, -55, 37], "bob"))

print("---------")

def delete_last(list):
    list = list[:-1]
    return list

print(delete_last([7, "joe", "apple", 9.81, False]))