n = int(input())
sum_of_chars = 0

for i in range(0, n):
    sum_of_chars += ord(input())
print(f"The sum equals: {sum_of_chars}")