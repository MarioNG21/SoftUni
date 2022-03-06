# когато е зелено за всяка секунда напуска един символ от името на колата
# като има свободен прозорец и колкото керактари са останали , бива удрян първия
# когато е зелено влизат и излизат пък когато е свободния прозорец могат само да излизат коли
from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
has_crashed = False
while True:
    command = input()
    if command == "green":
        current_green = green_light_duration
        while cars and current_green > 0:
            car = cars.popleft()
            if current_green >= len(car) or current_green + free_window_duration >= len(car):
                counter += 1
                current_green -= len(car)
            else:
                print("A crash happened")
                print(f'{car} ')
    else:
        cars.append(command)
