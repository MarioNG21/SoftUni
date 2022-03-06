command = input()
numbers = [int(x) for x in input().split()]

result = 0
if command == "Even":
    result = sum(filter(lambda x: x % 2 == 0, numbers))
else:
    result = sum(filter(lambda x: x % 2 == 1, numbers))

print(len(numbers) * result)
