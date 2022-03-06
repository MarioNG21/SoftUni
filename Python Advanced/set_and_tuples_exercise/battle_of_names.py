n = int(input())

even = set()
odd = set()

for row in range(1, n+1):
    name = input()
    name_sum = sum([ord(ch) for ch in name])
    final_result = name_sum // row
    if final_result % 2 == 0:
        even.add(final_result)
    else:
        odd.add(final_result)

even_sum = sum(even)
odd_sum = sum(odd)

result = set()

if even_sum == odd_sum:
    result = odd.union(even)
elif even_sum > odd_sum:
    result = odd.symmetric_difference(even)
else:
    result = odd.difference(even)

print(', '.join([str(x) for x in result]))