number_str = input().split()

numbers_inverted = []

for num in number_str:
    num_inverted = int(num) * -1
    numbers_inverted.apend(num_inverted)

print(numbers_inverted)