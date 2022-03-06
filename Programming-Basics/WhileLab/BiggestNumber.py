from sys import maxsize
max_number = -maxsize
command = input()
while command != "Stop":
    new_number = int(command)
    if new_number > max_number:
        max_number = new_number
    command = input()
else:
    print(max_number)