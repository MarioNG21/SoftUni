def contests_add(cont, user, points, current_contests):
    if cont not in current_contests:
        current_contests[cont] = {user: [points]}
    elif user not in current_contests[cont]:
        current_contests[cont][user] = [points]
    else:
        current_contests[cont][user].append(points)
    return current_contests


contests, total_users_points = {}, {}

command = input()
while command != "no more time":
    username, contest, current_points = command.split(" -> ")
    current_points = int(current_points)
    contests = contests_add(contest, username, current_points, contests)
    command = input()
a = 5
for c, items in contests.items():
    print(f"{c}: {len(contests[c])} participants")
    ind = 0

    for u, p in sorted(items.items(), key=lambda x: (-max(x[1]), x[0])):
        ind += 1
        print(f"{ind}. {u} <::> {max(p)}")

        if u not in total_users_points:
            total_users_points[u] = 0
        total_users_points[u] += max(p)

print(f"Individual standings:")
ind = 0

for name, pts in sorted(total_users_points.items(), key=lambda x: (-x[1], x[0])):
    ind += 1
    print(f"{ind}. {name} -> {pts}")