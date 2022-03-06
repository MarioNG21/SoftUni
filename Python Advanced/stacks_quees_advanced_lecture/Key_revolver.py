from collections import deque

bullet_price = int(input())
size_gun = int(input())
num_of_bullets = [int(x) for x in input().split()]
locks = [int(y) for y in input().split()]
value = int(input())
counter = 0

locks_queue = deque()
bullets_queue = deque()

for _ in locks:
    locks_queue.append(_)

for _ in num_of_bullets:
    bullets_queue.appendleft(_)


while bullets_queue:
    for time in range(size_gun):
        current_bullet = bullets_queue[0]
        current_lock = locks_queue[0]
        if current_lock >= current_bullet:
            bullets_queue.popleft()
            locks_queue.popleft()
            print('Bang!')
        else:
            print('Ping!')
            bullets_queue.popleft()
        counter += 1
    if bullets_queue:
        print('Reloading!')
    if not locks_queue or not bullets_queue:
        print(f"{len(bullets_queue)} bullets left. Earned ${value - (counter * bullet_price)}")
        break

if not bullets_queue and locks_queue:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")