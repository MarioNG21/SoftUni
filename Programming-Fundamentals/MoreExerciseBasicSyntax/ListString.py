word = input()
length = len(word)
position = -1
my_list = [ ]
for symbol in range (length):
    if str.isupper(word[symbol]):
        position += 1
        my_list.insert(position, symbol)

print(my_list)