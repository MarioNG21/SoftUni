string = input().split()
word_one = string[0]
word_two = string[1]

total_sum = 0

shorted_word_len = min(len(word_one), len(word_two))

for i in range(shorted_word_len):
    word_one_curr_ch = word_one[i]
    word_two_curr_ch = word_two[i]

    ch_sum = ord(word_one_curr_ch) * ord(word_two_curr_ch)

    total_sum += ch_sum

longer_word_length = max(len(word_one), len(word_two))
for i in range(shorted_word_len, longer_word_length):
    if len(word_one) > len(word_two):
        curr_word_ch = word_one[i]

    else:
        curr_word_ch = word_two[i]
    total_sum += ord(curr_word_ch)

print(total_sum)