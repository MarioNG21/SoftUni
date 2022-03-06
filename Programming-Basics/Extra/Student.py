from math import floor
#n = int(input())
#day_time = input()
#prize = 0
#if day_time == "day":
#    if n < 20:
#        prize = 0.7 + (0.79 * n)
#    if n >= 20 and n < 100 :
 #       prize = 0.09 * n
  #  if n >= 100:
   #     prize = 0.06 * n

#if day_time == "night":
 #   if n < 20:
  #      prize = 0.7 + (0.9 * n)
   # if n >= 20 and n < 100:
     #   prize = 0.09 * n
    #if n >= 100:
      #  prize = 0.06 * n

#print(f"{prize:.2f}")
n = int(input())
day_time = input()

if day_time == "day":
    if n < 20:
        prize_for_taxi = 0.7 + (0.79 * n)
        print(f"{prize_for_taxi:.2f}")
    if n >= 20 and n < 100:
        prize_for_bus = 0.09 * n
        print(f"{prize_for_bus:.2f}")
    if n >= 100:
        prize_for_train = 0.06 * n
        print(f"{prize_for_train:.2f}")

if day_time == "night":
    if n < 20:
        prize_for_taxi = 0.7 + (0.9 * n)
        print(f"{prize_for_taxi:.2f}")
    if n >= 20 and n < 100:
        prize_for_bus = 0.09 * n
        print(f"{prize_for_bus:.2f}")
    if n >= 100:
        prize_for_train = 0.06 * n
        print(f"{prize_for_train:.2f}")