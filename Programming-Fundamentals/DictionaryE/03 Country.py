country = input().split(", ")
capitals = input().split(", ")

country_capital_info = dict(zip(country, capitals))

for key, value in country_capital_info.items():
    print(f"{key} -> {value}")
