key = input().split()
command = input()

while not command == "find":
    new = ""
    while len(new) != len(command):
        for el in range(len(key)):
            value = int(key[el])
            for ch in command:
                new_letter = ord(ch) - value
                letter = chr(new_letter)
                new += letter
                value = key[el + 1]
    command = input()
