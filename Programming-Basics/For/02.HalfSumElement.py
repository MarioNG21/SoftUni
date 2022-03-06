# vuvejdane na n na broi chisla
# sumata na ostanalite = sumata na vsichki - max chislo
# maks chisloto
import sys
n = int(input()) # брой на числа
max = -sys.maxsize
sum = 0
for number in range(1, n+1):
    value = int(input())
    if value > max:
        max = value
    sum += value

sum_others = sum - max
if sum_others == max:
    print("Yes")
    print(f"Sum = {max}")
else:
    dif = abs(max - sum_others)
    print("No")
    print(f"Diff = {dif}")