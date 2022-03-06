movie = input()
rows = int(input())
column = int(input())

if movie == "Premiere":
    income = (rows * column) * 12
    print(f"{income:.2f}")
elif movie == "Normal":
    income = (rows * column) * 7.50
    print(f"{income:.2f}")
elif movie == "Discount":
    income = (rows * column) * 5
    print(f"{income:.2f}")
