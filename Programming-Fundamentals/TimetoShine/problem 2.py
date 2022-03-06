import re
pattern = r"!(?P<command>([A-Z][a-z]{2,}))!:\[(?P<string>([A-Za-z]{8,}))\]"
counter = int(input())
for i in range(counter):
    text = input()
    if re.search(pattern, text):
        matches = re.finditer(pattern, text)
        for match in matches:
            command = match.group("command")
            string = match.group("string")
            encrypted_message = []
            for ch in string:
                encrypted_message.append(str(ord(ch)))
            print(f"{command}: {' '.join(encrypted_message)}")
    else:
        print("The message is invalid")