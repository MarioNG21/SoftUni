from sys import maxsize
number = int(input())
max = -maxsize
min = maxsize
for numbers in range(1, number+1):
    value = int(input())
    if value > max:
        max = value
    if value < min:
        min = value
print(f"Max number: {max}")
print(f"Min number: {min}")