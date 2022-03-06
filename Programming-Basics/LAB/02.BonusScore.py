#начален брой точки = цяло число
#бонус точки -> наслагват се на началния брой
#Да се напише програма, която пресмята бонус точките, които получава числото и общия брой точки (числото + бонуса)
#ако е до 100 включително, бонус точките са 5
# ако е по голямо от 100, бонус точките са 20 проц от числото
#ако е по голямо от 1000, бонус точките са 10 проц от числото
#За четно число -> +1 т
#за число което завършва на 5 -> +2т

starting_points = int(input())
if starting_points <= 100:
    bonus_points = 5
    sum_points = starting_points + bonus_points

elif starting_points > 100 and starting_points <= 1000:
    bonus_points = starting_points * 0.2
    sum_points = starting_points + bonus_points

elif starting_points > 1000:
    bonus_points = starting_points * 0.1
    sum_points = starting_points + bonus_points

if starting_points % 2 == 0:
    bonus_points = bonus_points + 1
    sum_points = sum_points + 1

elif starting_points % 10 == 5:
    bonus_points = bonus_points + 2
    sum_points = sum_points + 2

print(bonus_points)
print(sum_points)
