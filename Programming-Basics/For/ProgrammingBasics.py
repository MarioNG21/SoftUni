number_pencils = int(input())
number_markers = int(input())
cleaning_material = float(input())
discount = int(input())

pencils = number_pencils * 5.80
markers = number_markers * 7.20
material = cleaning_material * 1.20

needed_money = pencils + markers + material
needed_money = needed_money - (discount / 100) * needed_money
print(f"{needed_money:.3f}")