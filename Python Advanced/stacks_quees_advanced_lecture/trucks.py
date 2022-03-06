from collections import deque

pumps_count = int(input())

queue = deque()

for _ in range(pumps_count):
    pump = [int(x) for x in input().split()]
    queue.append(pump)

for index in range(pumps_count):
    car_fuel = 0
    completed = True
    for pump in queue:
        petrol = pump[0]
        distance = pump[1]
        car_fuel += petrol

        if distance > car_fuel:
            completed = False
            break
        car_fuel -= distance
    if completed:
        print(index)
        break
    else:
        queue.append(queue.popleft())