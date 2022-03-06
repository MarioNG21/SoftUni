def get_round(sequence):
    return [round(x) for x in sequence]


nums = [float(x) for x in input().split()]
print(get_round(nums))