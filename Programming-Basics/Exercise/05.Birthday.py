hall_rent = int(input())
price_cake = 0.2 * hall_rent
price_drinks = price_cake - 0.45 * price_cake
price_animator = hall_rent / 3
expenses = hall_rent+price_cake+price_drinks+price_animator
print (expenses)