num_string = input().split()
inverted_num = []
for i in num_string:
    number_inverted = int(i) * -1

    inverted_num.append(number_inverted)

print(inverted_num)