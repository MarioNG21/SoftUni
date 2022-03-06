from collections import deque
potatoes = input().split(" ")
potatoes_queue = deque()
for p in potatoes:
    potatoes_queue.appendleft(p)
step = int(input())

while True:

    for _ in range(step - 1):
        potatoes_queue.appendleft(potatoes_queue.pop())
    potatoes_to_remove = potatoes_queue.pop()

    if potatoes_queue:
        print(f"Removed {potatoes_to_remove}")
    else:
        print(f"Last is {potatoes_to_remove}")
        break