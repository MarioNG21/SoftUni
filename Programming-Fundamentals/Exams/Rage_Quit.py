rage_message = input()
unique_letters = ''
new_message = ''
num = ''
for ch in range(len(rage_message)):
    if not rage_message[ch].isdigit():
        new_message += rage_message[ch]
        continue

    if ch != (len(rage_message) - 1) and rage_message[ch+1].isdigit():
        num += rage_message[ch]
        continue

    num += rage_message[ch]
    unique_letters += new_message.upper() * int(num)
    new_message = ''
    num = ''

print(f"Unique symbols used: {len(set(unique_letters))}")
print(unique_letters)
