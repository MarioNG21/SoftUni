first_set_counter, second_set_counter = [int(x) for x in input().split()]

set1 = set()
set2 = set()

for _ in range(first_set_counter):
    set1.add(int(input()))

for i in range(second_set_counter):
    set2.add(int(input()))


[print(x) for x in set1 & set2]

