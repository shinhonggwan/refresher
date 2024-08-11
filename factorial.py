# honggwan shin

def sort_two_strings(string1, string2):
    if string1.upper() < string2.upper():
        return string1, string2
    else:
        return string2, string1

print(sort_two_strings("aardvark", "Zebra"))
print(sort_two_strings("Byron", "Lovelace"))


