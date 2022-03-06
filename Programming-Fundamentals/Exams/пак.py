contests, users = {}, {}

command = input()
while command != "end of contests":
    contest, password = command.split(":")
    contests[contest] = password
    command = input()

command = input()
while command != "end of submissions":
    contest, password, username, points = command.split('=>')
    points = int(points)

    if contest not in contests or contests[contest] != password:
        command = input()
        continue

    if username not in users:
        users[username] = {contest: points}
    elif contest not in users[username]:
        users[username].update({contest: points})
    elif users[username][contest] < points:
        users[username][contest] = points

    command = input()

best_candidates = {u: sum(i.values()) for u, i in users.items()}
best_user, max_points = '', 0

for u, p in best_candidates.items():
    if p > max_points:
        max_points = p
        best_user = u

print(f"Best candidate is {best_user} with total {max_points} points.\n"
      f"Ranking:")

for u, i in sorted(users.items()):
    print(u)
    for c, p in sorted(i.items(), key=lambda x: -x[1]):
        print(f"#  {c} -> {p}")
