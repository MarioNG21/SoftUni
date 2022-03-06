number = int(input())

positive_nums = []
negative_nums = []
for n in range(number):
    new_number = int(input())
    if new_number >= 0:
        positive_nums.append(new_number)
    else:
        negative_nums.append(new_number)
print(positive_nums)
print(negative_nums)

print(f"Count of positives: {len(positive_nums)}. Sum of negatives: {sum(negative_nums)}")
