# ресто в лв -> ресто * 100 ->  в стотинки
# Повтаряме :
#               1. проверка с коя монета мога да върна
#               2. връщаме рество с тази монета => ресто -= стойностт
#
#
#
from math import floor
change = floor(float(input()) * 100) # ресто в стотинки
count = 0 # броя на монетите
while change > 0:
    if change >= 200:
        change -= 200
        count += 1
    elif change >= 100:
        change -= 100
        count +=1
    elif change >= 50:
        change -= 50
        count += 1
    elif change >= 20:
        change -= 20
        count +=1
    elif change >= 10:
        change -= 10
        count += 1
    elif change >= 5:
        change -= 5
        count += 1
    elif change >= 2:
        change -= 2
        count += 1
    elif change >= 1:
        change -= 1
        count += 1
else:
    print(count)