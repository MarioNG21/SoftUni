n = int(input())

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

prime = []
secondary = []

for r in range(n):
    prime.append(matrix[r][r])
    secondary.append(matrix[r][n - r - 1])

sum_prime = sum(prime)
sum_secondary = sum(secondary)

print(abs(sum_prime - sum_secondary))
