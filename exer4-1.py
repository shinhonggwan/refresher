# Write code that asks the user for two numbers
# and then prints out "The result is" followed by
# the result of multiplying those numbers.
# 3, 20
# 60
result = 0

def multiply():

    print("Please enter two number seperated by a , ")
    userinput = input()

    num1, num2 = map(float, userinput.split(","))

    result = num1 * num2

    return result

print(result)
print(multiply())