counter = int(input())
parking_lot = set()

for _ in range(counter):
    direction, car_number = input().split(', ')
    if direction == "IN":
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)

if not parking_lot:
    print("Parking Lot is Empty")
else:
    [print(car) for car in parking_lot]