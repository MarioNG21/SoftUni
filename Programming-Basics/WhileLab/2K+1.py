number = int(input())
new_numbers = 0
while new_numbers <= number:
        new_numbers = (2 * new_numbers) + 1
        if new_numbers > number:
            break
        print(new_numbers)