from sys import maxsize
number_one = int(input())
number_two = int(input())
max_fourth_symbol = -maxsize
for symbol_one in range(1, number_one+1):
    for symbol_two in range(1, number_one+1):
        for symbol_three in range(1, number_two+1):
            value = chr(symbol_three)
            for symbol_four in range(1, number_two+1):
                value_two = chr(symbol_four)
                for symbol_five in range(1, number_one+1):
                    if symbol_five > max_fourth_symbol:
                        max_fourth_symbol = symbol_five
                    print(f"{symbol_one}{symbol_two}{value}{value_two}{max_fourth_symbol}", end=" ")