# четен ден и нечетен час 2,5
# нечетен ден и четен час 1.25
# всеки друг случай е 1
days = int(input())
hours = int(input())
sum_price = 0
for day in range(1, days+1):
    price = 0
    for hour in range(1, hours+1):
        if day % 2 == 0 and hour % 2 == 1:
            price += 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            price += 1.25
        else:
            price += 1
    sum_price += price
    print(f"Day: {day} - {price:.2f} leva")
else:
    print(f"Total: {sum_price:.2f} leva")