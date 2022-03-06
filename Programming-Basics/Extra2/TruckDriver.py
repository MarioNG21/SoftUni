season = input()
km_per_season = float(input())
whole_sum = 0
if season == "Autumn" or season == "Spring":
    if km_per_season <= 5000:
        price_per_km = 0.75
    elif 5000 < km_per_season <= 10000:
        price_per_km = 0.95
    elif 10000 < km_per_season <= 20000:
        price_per_km = 1.45
    whole_sum = 4 * price_per_km * km_per_season
    taxes = 0.10 * whole_sum
    whole_sum = whole_sum - taxes
if season == "Summer":
    if km_per_season <= 5000:
        price_per_km = 0.90
    elif 5000 < km_per_season <= 10000:
        price_per_km = 1.10
    elif 10000 < km_per_season <= 20000:
        price_per_km = 1.45
    whole_sum = 4 * price_per_km * km_per_season
    taxes = 0.10 * whole_sum
    whole_sum = whole_sum - taxes
if season == "Winter":
    if km_per_season <= 5000:
        price_per_km = 1.05
    elif 5000 < km_per_season <= 10000:
        price_per_km = 1.25
    elif 10000 < km_per_season <= 20000:
        price_per_km = 1.45
    whole_sum = 4 * price_per_km * km_per_season
    taxes = 0.10 * whole_sum
    whole_sum = whole_sum - taxes
print(f"{whole_sum:.2f}")