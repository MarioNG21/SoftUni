key = input().split()

command = input()
while not command == "find":
    new_string = []
    for el in command:
        ascii_el = ord(el)
        for i in key:
            ascii_el -= int(i)
        new_string.append(chr(ascii_el))
    command = input()