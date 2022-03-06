steps = 10000
command = input()
sum_steps = 0
while command != "Going home":
    done_steps = int(command)
    sum_steps += done_steps
    if sum_steps >= steps:
        break
    command = input()
else:
    steps_to_home = int(input())
    sum_steps += steps_to_home
if sum_steps >= steps:
    diff = abs(steps - sum_steps)
    print("Goal reached! Good job!" )
    print(f"{diff} steps over the goal!" )
else:
    diff = abs(sum_steps - steps)
    print(f"{diff} more steps to reach goal.")