def replace_character_code(word: str):
    ch_code_st = ""
    new_word = []

    for ch in word:
        if ch.isnumeric():
            ch_code_st += ch
        else:
            new_word.append(ch)

    ch_at_beginning = chr(int(ch_code_st))

    new_word.insert(0, ch_at_beginning)

    return new_word


def decipher_word(word: str):
    new_word = replace_character_code(word)

    new_word[1], new_word[-1] = new_word[-1], new_word[1]

    return ''.join(new_word)


words = input().split()

decipher_words = [decipher_word(word) for word in words]


print(' '.join(decipher_words))