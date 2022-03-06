box_of_clothes = [int(x) for x in input().split()]
capacity = int(input())
sum_of_clothes = 0

counter = 1

while True:
    if not box_of_clothes:

        break
    cloth = box_of_clothes.pop()

    sum_of_clothes += cloth

    if sum_of_clothes >= capacity:
        counter += 1
        if sum_of_clothes > capacity:
            box_of_clothes.append(cloth)

        sum_of_clothes = 0

print(counter)