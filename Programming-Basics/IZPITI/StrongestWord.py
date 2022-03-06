from sys import maxsize
max_value = -maxsize
command = input()
winner_word = ""
while command != "End of words":
    word = command
    word_length = len(word)
    value = 0
    for n in range(word_length):
        value += ord(word[n])
    if word[0] == "a" or word[0] == "A" or word[0] == "e" or word[0] == "E" or word[0] == "i" or word[0] == "I" or word[0] == "o" or word[0] == "O" or word[0] == "u" or word[0] == "U" or word[0] == "y" or word[0] == "Y":
        value = value * word_length
    else:
        value = round(value/word_length)
    if value > max_value:
        max_value = value
        winner_word = word
    command = input()
else:
    print(f"The most powerful word is {winner_word} - {max_value}" )