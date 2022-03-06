egg_in_start = int(input())
command = input()
bought_eggs = 0
while command != "Close":
    buy_or_fill = command
    number_of_eggs = int(input())
    if buy_or_fill == "Buy":
        if number_of_eggs > egg_in_start:
            print("Not enough eggs in store!")
            print(f"You can buy only {egg_in_start}.")
            break
        egg_in_start -= number_of_eggs
        bought_eggs += number_of_eggs
    else:
        egg_in_start += number_of_eggs
    command = input()
else:
    print("Store is closed!")
    print(f"{bought_eggs} eggs sold.")
