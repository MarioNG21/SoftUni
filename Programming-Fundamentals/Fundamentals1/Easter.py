# 1 pack eggs = 75 % ot 1kg flour
# 1 kg Flour =
#  0.250ml Milk = 25 more than the price for 1 kg flour
# 3 colored eggs for 1 cozonac
# lose some colored eggs after this formula cozonac - ((curent cozonac number)-2)
budget = float(input())
one_kg_flour_price = float(input())
eggs_price = 0.75 * one_kg_flour_price
milk_price_for_250ml = 1.25 * one_kg_flour_price / 4
cozonacs_counter = 0
colored_egg = 0
one_cozonac_price = one_kg_flour_price + eggs_price + milk_price_for_250ml
while budget - one_cozonac_price > 0:
    budget -= one_cozonac_price
    cozonacs_counter += 1
    colored_egg += 3
    if cozonacs_counter % 3 == 0:
        colored_egg -= cozonacs_counter - 2

print(f"You made {cozonacs_counter} cozonacs! Now you have {colored_egg} eggs and {budget:.2f}BGN left.")
