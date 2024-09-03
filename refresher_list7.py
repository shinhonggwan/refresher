def mean(num_list):
    """Return the mean value of the numbers in num_list"""
    sum = 0
    for num in num_list:
        sum += num
    return sum / len(num_list)

print(mean([5, 7, 22, 16, 3, 11]))

def roots_of_perfect_squares(num_list):
    """returns the square roots of the perfect squares in num_list, in sorted order"""
    new_list = []
    for num in num_list:
        root = num ** 0.5
        if num == int(root + 0.5) ** 2:
            new_list += [int(root)]
    return sorted(new_list)

print(roots_of_perfect_squares([81,70,22,26,24,49,23,9]))