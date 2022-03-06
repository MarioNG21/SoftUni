from sys import maxsize
command = input()
max_points = - maxsize
winner_name = ""
while command != "Stop":
    name = command
    text_length = len(name)
    points = 0
    for number in range(text_length):
        numbers = int(input())
        if numbers == ord(name[number]):
            points += 10
        else:
            points += 2
    if points >= max_points:
        max_points = points
        winner_name = name
    command = input()
else:
    print(f"The winner is {winner_name} with {max_points} points!")