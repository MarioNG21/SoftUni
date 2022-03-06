numbers = [int(x) for x in input().split()]

sum_positiv = sum([int(x) for x in numbers if x >0])
sum_negativ = sum([int(x) for x in numbers if x <0])

print(sum_negativ)
print(sum_positiv)

if abs(sum_positiv) > abs(sum_negativ):
    print('The positives are stronger than the negatives')
else:
    print("The negatives are stronger than the positives")