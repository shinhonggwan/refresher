#honggwan shin

gem = "onyx"
dino = "velociraptor"
fruit = "strawberry"
hero = "spiderman"
poem = "mary had a little lamb"


print(fruit[2:5])
print(hero[:6])
print(hero[6:])
print(hero[:])
print(hero[::2])
print(hero[::-1])

print("-----------")
"""A palindrome is a string that reads the same 
forward or backward. Write a function called is_pal 
that takes a string parameter and returns True if that 
string is a palindrome, but returns False otherwise."""

def is_plaindrome(word):
    word = word.lower()

    return word == word[::-1]

print(is_plaindrome("hello"))
print(is_plaindrome("civic"))
