rage_message = input()
final_text = ""
unique_symbols = []
message_list = []
index = -1
multy_list = []
for i in rage_message:
    index += 1
    if not i.isdigit():
        unique_symbols.append(i.lower())
        message_list.append(i)
    else:
        multyplayer = int(i)
        multy_list.append(multyplayer)
        if index != len(rage_message)-1:
            if rage_message[index+1].isdigit():
                multy_list.append(rage_message[index+1])
                multyplayer = int(''.join(message_list))
        text = ''.join(message_list).upper()
        final_text += text * multyplayer
        message_list = []

counter = set(unique_symbols)
print(f"Unique symbols used: {len(counter)}")
print(final_text)