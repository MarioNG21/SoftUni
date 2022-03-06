# всяка четна година от 1800 до .... (1802) ще харчи по 12 000 на година
# всяка нечетна година ще харчи по 12 000 + 50 *(навършените от него години на дадената година)
# на 18 години е иванчо
#
#
#

inherited_money = float(input())
years_till_dead = int(input())
present_years = 17
for year in range(1800, years_till_dead+1):
    present_years += 1
    if year % 2 == 0:
        inherited_money -= 12000
    elif year % 2 != 0:
        inherited_money = inherited_money - (12000 + (50 * present_years))
if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    inherited_money = abs(inherited_money)
    print(f"He will need {inherited_money:.2f} dollars to survive.")