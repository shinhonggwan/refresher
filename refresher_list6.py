def translate_single_word(word):
    """translates a single English word to Pig Latin"""
    vowels = 'aeiou'
    if word[0] in vowels:
        return word + 'ay'
    else:
        index = 0
        while index < len(word) and word[index] not in vowels:
            index += 1
        return word[index:] + word[0:index] + 'ay'

def translate(text):
    """Translate English text to Pig Latin"""
    new_text = ''
    word_list = text.split()
    for word in word_list:
        new_text += translate_single_word(word) + ' '
    return new_text

print(translate("look at me still talking when there's science to do"))