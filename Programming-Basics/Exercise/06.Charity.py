 #torta 45 lv
#gofreta 5.80 lv
#palachinka 3.20 lv
#1/8
number_capagne_days = int(input())
number_bakers = int(input())
number_cakes = int(input())
number_waffles = int(input())
number_pancakes = int(input())

cakes = number_cakes * 45
waffles = number_waffles * 5.80
pancakes = number_pancakes * 3.20

total_per_one_baker = cakes + waffles + pancakes
total = total_per_one_baker * number_bakers
total_whole_capagne = number_capagne_days * total
sum = total_whole_capagne - 1/8 * total_whole_capagne
print(sum)

