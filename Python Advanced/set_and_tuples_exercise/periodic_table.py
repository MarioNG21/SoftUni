counter = int(input())

el_set = set()

for _ in range(counter):
    current_el = set(input().split())
    el_set = el_set | current_el

[print(x) for x in el_set]