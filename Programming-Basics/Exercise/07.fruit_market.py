price_strawberries = float(input())
quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberries = float(input())
quantity_strawberries = float(input())

# цена за ягод
total_strawberries = quantity_strawberries * price_strawberries
# цена за малини
price_raspberries = price_strawberries / 2
total_raspberries = quantity_raspberries * price_raspberries
#цена за банани
price_bananas = price_raspberries - price_raspberries * 0.8
total_bananas = quantity_bananas * price_bananas
#цена на протокалите
price_oranges = price_raspberries - price_raspberries * 0.4
total_oranges = quantity_oranges * price_oranges

expenses = total_strawberries+total_raspberries+total_bananas + total_oranges
print(expenses)