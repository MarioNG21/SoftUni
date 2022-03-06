import sys
number = int(input())
odd_max = -sys.maxsize
odd_min = sys.maxsize
even_max = -sys.maxsize
even_min = sys.maxsize
sum_odd = 0
sum_even = 0
for numbers in range(1, number+1):
    value = float(input())
    if numbers % 2 != 0:
        if value > odd_max:
            odd_max = value
        if value < odd_min:
            odd_min = value
        sum_odd += value
    elif numbers % 2 == 0:
        if value > even_max:
            even_max = value
        if value < even_min:
            even_min = value
        sum_even += value

print(f"OddSum={sum_odd:.2f},")
if odd_min == sys.maxsize:
    print("OddMin=No",)
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -sys.maxsize:
    print("OddMax=No",)
else:
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={sum_even:.2f},")
if even_min == sys.maxsize:
    print("EvenMin=No",)
else:
    print(f"EvenMin={even_min:.2f}," )
if even_max == -sys.maxsize:
    print("EvenMax=No",)
else:
    print(f"EvenMax={even_max:.2f}" )
