def first_word(string):
    temp = []
    for word in gather(string):
        checked = check(word)
        if checked in temp:
            return checked
        else:
            temp.append(checked)

def check(word):
    index = 0
    new_word = ''
    for char in word:
        index += 1
        if char == ',':
            return new_word.lower()
        else:
            new_word = f'{new_word}{char}'
    return new_word.lower()

def gather(string):
    words = []
    chars = []
    word = ''
    for i in string:
        if i == ' ':
            words.append(word)
            word = ''
        else:
            word = f'{word}{i}'
    if word != '':
        words.append(word)
    return words