number_str = input().split()
n = int(input())

for i in range(len(number_str)):
    number_str[i] = int(number_str[i])

for j in range(n):
    min_element = min(number_str)

    number_str.remove(min_element)

for i in range(len(number_str)):
    number_str[i] = str(number_str[i])

print(", ".join(number_str))