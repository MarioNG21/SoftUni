factor = int(input())
count = int(input())
new_list = []
for num in range(1, count+1):
    new_number = num * factor
    new_list.append(new_number)

print(new_list)
