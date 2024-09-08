members = ["Tommy", "Johnny", "Joey", "Dee Dee"]
birds = ["starling", "blue jay", "wood packer", "ostrich", "chicken"]

print(members)
members[0] = "Marky"
print(members)

print(birds)
birds[1:3] = ["robin", "chickadee"]
print(birds)

birds[1:3] = ["hummingbird", "wren", "emu", "penguin"]
print(birds)
birds[3:6] = ["cassowary"]
print(birds)
birds[1:1] = ["kiwi", "big bird"]
print(birds)
birds[2:3] = []
print(birds)

birds_copy_1 = birds[:]
birds_copy_2 = list(birds)

print("-------")
print(birds_copy_1)
print(birds_copy_2)
print("-------")

vocab_words = []
vocab_words.append("usagi")
vocab_words.append("inazuma")
vocab_words.append("hebi")
vocab_words.append("kitsune")
print(vocab_words)
del vocab_words[2]
print(vocab_words)

"""
def square_val(val):
    val[0] = val[0] * val[0]
    print(val)

num_list = [8]
square_val(num_list)
print(num_list)
"""
