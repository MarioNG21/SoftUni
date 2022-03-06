
a1 = int(input())
a2 = int(input())
n = int(input())
# simvol 1
for symbol_one in range(a1, (a2-1)+1):
    # simvol 2
    for symbol_two in range(1, (n-1)+1):
        for symbol_three in range(1, int((n / 2) - 1)+ 1):
            value = chr(symbol_one)
            value_two = symbol_two
            value_three = symbol_three
            symbol_four = ord(value)
            if ord(value) % 2 != 0:
                if (value_two + value_three + symbol_four) % 2 == 1:
                    print(f"{value}-{value_two}{value_three}{symbol_four}")