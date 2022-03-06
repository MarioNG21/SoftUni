counter = int(input())
cars = {}

for _ in range(counter):
    car_input_args = input().split('|')
    cars[car_input_args[0]] = [int(car_input_args[1]), int(car_input_args[2])]

max_fuel = 75

while True:
    command = input()
    if command == "Stop":
        break
    cmd_arg = command.split(" : ")
    action = cmd_arg[0]
    car_name = cmd_arg[1]
    car_data = cars[car_name]
    if action == "Drive":
        distance = int(cmd_arg[2])
        fuel = int(cmd_arg[3])

        if car_data[1] < fuel:
            print("Not enough fuel to make that ride")
            continue

        car_data[0] += distance
        car_data[1] -= fuel
        print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if car_data[0] >= 100_000:
            print(f"Time to sell the {car_name}!")
            cars.pop(car_name)

    elif action == "Refuel":
        fuel = int(cmd_arg[2])
        old_fuel = car_data[1]
        car_data[1] += fuel
        fuel_to_show = fuel
        if car_data[1] > max_fuel:
            fuel_to_show = max_fuel - old_fuel
            car_data[1] = max_fuel

        print(f"{car_name} refueled with {fuel_to_show} liters")

    elif action == "Revert":
        km = int(cmd_arg[2])
        car_data[0] -= km

        if car_data[0] < 10_000:
            car_data[0] = 10_000
            continue

        print(f"{car_name} mileage decreased by {km} kilometers")

for name, data in sorted(cars.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{name} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.")