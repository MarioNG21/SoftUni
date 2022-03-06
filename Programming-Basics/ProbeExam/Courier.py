weight_in_kg = float(input())
service = input()
distance_in_km = int(input())
price_shipping = 0
if service == "standard":
    price = 0
    if weight_in_kg < 1:
        price = 3
    elif 1 < weight_in_kg < 10:
        price = 5
    elif 10 <= weight_in_kg < 40:
        price = 10
    elif 40 <= weight_in_kg < 90:
        price = 15
    elif 90 <= weight_in_kg < 150:
        price = 20
    price_shipping = price * distance_in_km
    price_shipping = price_shipping / 100
elif service == "express":
    price = 0
    if weight_in_kg < 1:
        price = 3
        price_with_add = (3 * 0.8) * weight_in_kg
    elif 1 < weight_in_kg < 10:
        price = 5
        price_with_add = (0.4 * 5) * weight_in_kg
    elif 10 <= weight_in_kg < 40:
        price = 10
        price_with_add = (0.05 * 10) * weight_in_kg
    elif 40 <= weight_in_kg < 90:
        price = 15
        price_with_add =  (0.02 * 15) * weight_in_kg
    elif 90 <= weight_in_kg < 150:
        price = 20
        price_with_add =  (0.01 * 20) * weight_in_kg
    price_shipping_normal = price * distance_in_km
    price_shipping_with_add = price_with_add * distance_in_km
    price_shipping = price_shipping_with_add + price_shipping_normal
    price_shipping = price_shipping / 100
print(f"The delivery of your shipment with weight of {weight_in_kg:.3f} kg. would cost {price_shipping:.2f} lv.")