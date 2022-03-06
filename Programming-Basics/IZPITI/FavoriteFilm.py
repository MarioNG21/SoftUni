command = input()
from sys import maxsize
max_points = - maxsize
counter = 0
winner_name = ""
while command != "STOP":
    movie_name = command
    length_name = len(movie_name)
    sum = 0
    counter += 1
    if counter >= 7:
        print("The limit is reached.")
        break
    for letter in range(length_name):
        value = ord(movie_name[letter])
        if str.isupper(movie_name[letter]):
            value -= length_name
        if str.islower(movie_name[letter]):
            value -= 2 * length_name
        sum += value
    if sum > max_points:
        max_points = sum
        winner_name = movie_name
    command = input()
print(f"The best movie for you is {winner_name} with {max_points} ASCII sum.")