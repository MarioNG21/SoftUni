amount_of_numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
for numbers in range(1, amount_of_numbers+1):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1
p1_in_per = (p1 / amount_of_numbers) * 100
p2_in_per = (p2 / amount_of_numbers) * 100
p3_in_per = (p3 / amount_of_numbers) * 100
print(f"{p1_in_per:.2f}%")
print(f"{p2_in_per:.2f}%")
print(f"{p3_in_per:.2f}%")
