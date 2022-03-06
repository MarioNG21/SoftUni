ch_one = input()
ch_two = input()
text = input()

ascii_ch_one = ord(ch_one)
ascii_ch_two = ord(ch_two)
ascii_sum = 0

for el in range(0, len(text)):
    letter = text[el]
    ascii_letter = ord(letter)
    if ascii_ch_one < ascii_letter < ascii_ch_two:
        ascii_sum += ascii_letter

print(ascii_sum)