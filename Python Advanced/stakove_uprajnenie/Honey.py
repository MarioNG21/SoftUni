from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

operation = {'+': lambda a, b: abs(a + b),
             '-': lambda a, b: abs(a - b),
             '*': lambda a, b: abs(a * b),
             '/': lambda a, b: abs(a / b)
             }


total_honey = 0
while working_bees and nectar:
    bee = working_bees[0]
    nec = nectar[-1]
    current_symbol = symbols[0]

    if bee > nec:
        nectar.pop()
        continue
    else:
        if current_symbol in operation:
            if nec > 0:
                result = operation[current_symbol](bee, nec)
                total_honey += result
                symbols.popleft()
                working_bees.popleft()
                nectar.pop()
            else:
                symbols.popleft()
                working_bees.popleft()
                nectar.pop()
print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")