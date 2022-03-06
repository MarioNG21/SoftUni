# X площ от лозето -> 40% от реколтата за производство на вино
# Y кг. грозде  от 1кв.м лозе
# 1 литър вино се нужда 2.5 кг грозде
# Z желаното количество вино за продан
# Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно
# Ако е достатъчно, остатъкът се разделя по равно между работниците на лозето


import math
X = int(input())
Y = float(input())
Z = int(input())
number_of_workers = int(input())
sum_of_all = X * Y
wine = (sum_of_all * 0.4) / 2.5

if wine < Z:
    needed_wine = Z - wine
    print(f"It will be a tough winter! More {math.floor(needed_wine)} liters wine needed.")
else:
    needed_wine = wine - Z
    wine_pro_worker = needed_wine / number_of_workers
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(needed_wine)} liters left -> {math.ceil(wine_pro_worker)} liters per person.")