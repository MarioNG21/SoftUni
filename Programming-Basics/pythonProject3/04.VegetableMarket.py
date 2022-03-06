price_vegetable_for_kg = float(input())
price_fruits_for_kg = float(input())
sum_vegetable_kg = int(input())
sum_fruits_kg = int(input())

vegetable = price_vegetable_for_kg * sum_vegetable_kg
fruits = price_fruits_for_kg * sum_fruits_kg

whole_sum = (vegetable + fruits) / 1.94


print(f"{whole_sum:.2f}")