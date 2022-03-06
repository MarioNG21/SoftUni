n = int(input())

matrix = []
primary_sum = 0
secondary_sum = 0
for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
prime_el = []
sec_el = []

for r in range(n):
    primary_sum += matrix[r][r]
    secondary_sum += matrix[r][n - r - 1]
    prime_el.append(matrix[r][r])
    sec_el.append(matrix[r][n - r - 1])

print(f"Primary diagonal: {', '.join([str(x) for x in prime_el])}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join([str(x) for x in sec_el])}. Sum: {secondary_sum}")

