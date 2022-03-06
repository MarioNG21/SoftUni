first = input().split("|")

result = []

for idx in range(len(first) - 1, -1, -1):
    new_el = first[idx].split()
    result += new_el

print(*result)