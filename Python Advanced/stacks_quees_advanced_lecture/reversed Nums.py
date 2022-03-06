numbers = input().split(' ')
stack_nums = []
while numbers:
    new_num = numbers.pop()
    stack_nums.append(new_num)

print(' '.join(stack_nums))
