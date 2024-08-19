some_primes = [2,3,5,7,11,13,17,19,23,29,31]
some_names = ["Groucho", "Harpo", "Chico", "Zeppo", "Karl"]
some_stuff = [98, "Fido", -34.925, ["Phantom", "Tollbooth"]]
one = ["just me"]
zero = []

print(len(["Mary", "had", "a", "little", "lamb"]))
count = [1,2,3,4,5]
print(len(count))
print("--------")
print(some_primes[2])
print(some_primes[0:20:2])
print(some_names[::-2])
print("--------")
print(some_stuff[3])
print(some_stuff[3][1])
print(some_stuff[3][1][0])
print("--------")
print(13 in some_primes)
print(13 not in some_primes)
print("Fido" in some_stuff)
print("Phantom" in some_stuff)
print("Phantom" in some_stuff[3])
