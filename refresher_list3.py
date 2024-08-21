fun_floats = [3.141, 2.718, 6.283, 1.618, 1.414, 2.502, 0.577, 1.303, 2.685, 1.282]

for number in fun_floats:
    print(number)

print("----------")

total = 0
for number in fun_floats:
    total += number
print(total)

print("----------")

sentence = "Not the comfy chair!"
word_list = sentence.split()
print(word_list)

print("----------")

sentence2 = "The cat, a stray tabby, climbed in the window, tail twitching."
word_list2 = sentence2.split(", ")
print(word_list2)

print("----------")

fun_floats_doubled = [2 * x for x in range(1, 11) if x % 2 == 1]
print(fun_floats_doubled)

print("----------")

nums = [1,2,3,4,5,6,7,8,9]
filtered_nums = [x for x in nums if x % 3 == 0]
print(filtered_nums)
