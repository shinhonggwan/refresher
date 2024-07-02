num_years = 6
print("Enter the principle amount.")
original_principle = float(input())
print("Enter the annual interest rate as a percentage.")
interest_rate = float(input()) / 100
print("Enter the number of compounding periods per year.")
num = int(input())
new_principle = original_principle * ((1 + interest_rate / num) ** (num * num_years))
print("After " + str(num_years) + " years, the principle has grown from $" + str(original_principle) + " to $" + str(new_principle) + ".")
