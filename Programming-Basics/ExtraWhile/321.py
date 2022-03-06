command = input()
time_for_n = 0
time_for_c = 0
time_for_o = 0
letter = ""
word = ""
time_zero = 1
while command != "End":
    letter = command
    encode_command = letter.encode("ascii", "ignore")
    decoded_command = encode_command.decode()
    if letter == "n" and time_for_n <= 1:
        letter = ""
        time_for_n += 1
        time_zero += 1
    elif letter == "n" and time_for_n > 1:
        letter = "n"
    if letter == "c"and time_for_c <= 1:
        letter = ""
        time_for_c += 1
        time_zero += 1
    elif letter == "c" and time_for_c > 1:
        letter = "c"
    if letter == "o" and time_for_o <= 1:
        letter = ""
        time_for_o += 1
        time_zero += 1
    elif letter == "o" and time_for_o > 1:
        letter = "o"

    word += letter
    command = input()
else:
    print(word)