def swap_case(text):
    """Swap the case of all letters in a string"""
    new_str = ''
    for character in text:
        if 'A' <= character <= 'Z':
            new_str += character.lower()
        else:
            new_str += character.upper()
    return new_str

print(swap_case("Today is John Connor's birthday."))

def splice(text, target):
    """Remove occurences of the target from the text"""
    if target not in text:
        return text
    starting_at = 0
    new_text = ""
    while starting_at < len(text):
        index = text.find(target, starting_at)
        # if the target is in the remaining part of the text
        if index != -1:
            new_text += text[starting_at:index]
            starting_at = index + len(target)
        # if the target wasn't in the remaining part of the text
        else:
            new_text += text[starting_at:]
            starting_at = len(text)
    return new_text

words = "Cindy felt an intense abdominal pain"
print(splice(words, 'in'))

