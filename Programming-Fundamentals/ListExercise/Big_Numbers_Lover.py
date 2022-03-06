
numbers = [int(num) for num in input().split()]


numbers = numbers[::-1]
#max_number = - sys.maxsize
#####

for i in numbers:
    if i == 0:
        numbers.append(i)
    print(i, end="")
