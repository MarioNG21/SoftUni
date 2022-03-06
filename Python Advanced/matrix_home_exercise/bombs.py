from collections import deque

bomb_effect = deque([int(x) for x in input().split(',')])
bomb_casings = [int(x) for x in input().split(',')]


datura_bomb = 0
cherry_bomb = 0
smoke_bomb = 0

collected = False
while bomb_effect:
    if not bomb_casings:
        break
    current_effect = bomb_effect.popleft()
    current_casing = bomb_casings.pop()
    sum_bomb = current_effect + current_casing
    if sum_bomb == 40:
        datura_bomb += 1
    elif sum_bomb == 60:
        cherry_bomb += 1
    elif sum_bomb == 120:
        smoke_bomb += 1
    else:
        bomb_casings.append(current_casing - 5)
        bomb_effect.appendleft(current_effect)
    if datura_bomb >= 3 and smoke_bomb >= 3 and cherry_bomb >= 3:
        collected = True
        break
if collected:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effect:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effect])}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")

print(f"Cherry Bombs: {cherry_bomb}")
print(f"Datura Bombs: {datura_bomb}")
print(f"Smoke Decoy Bombs: {smoke_bomb}")
