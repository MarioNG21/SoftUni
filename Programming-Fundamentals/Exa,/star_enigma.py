import re
number = int(input())
pattern = r'[\@\!\:\>]*?@(?P<name>([A-Z][a-z]+))([0-9])?[\@\!\:\>\-]*?\:(?P<population>([0-9]+))[\@\!\:\>\-]*?\!(?P<action>([A|D]))\![\@\!\:\>]*?\->(?P<soldier>([0-9]+))'
message_dict_attack = []
message_dict_destroy = []
for i in range(number):
    message = input()
    encrypted_list = ['s', 't', 'a', 'r']
    decrypted_message = []
    counter = 0
    for el in message:
        el = el.lower()
        if el in encrypted_list:
            counter += 1
    for ch in range(len(message)):
        single_letter = message[ch]
        ascii_letter = ord(single_letter)
        ascii_letter -= counter
        decrypted_message.append(chr(ascii_letter))
    decrypted_message_new = ''.join(decrypted_message)
    matches = re.finditer(pattern, decrypted_message_new)
    for match in matches:
        name = match.group('name')
        state = match.group('action')
        if state == "A":
            message_dict_attack.append(name)
        elif state == "D":
            message_dict_destroy.append(name)


a = 5
print(f"Attacked planets: {len(message_dict_attack)}")
for i in sorted(message_dict_attack):
    print(f"-> {i}")

print(f"Destroyed planets: {len(message_dict_destroy)}")
for j in sorted(message_dict_destroy):
    print(f"-> {j}")
