field = dict()
individuals = dict()
ring_scores = dict()
while True:
    info = input().split(" -> ")
    if info[0] == "no more time":  # no more time
        break
    username, contest, points = info[0], info[1], int(info[2])

    if contest not in field:
        field[contest] = list()
    if username not in field[contest]:
        field[contest].append(username)

    if username not in individuals:
        individuals[username] = 0
    individuals[username] += points

    ring = (username, contest)
    if ring not in ring_scores:
        ring_scores[ring] = 0
    if ring_scores[ring] < points:
        individuals[username] -= ring_scores[ring]
        ring_scores[ring] = points
    else:
        individuals[username] -= points

ring_scores = sorted(ring_scores.items(), key=lambda x: (-x[1], x[0][0]))
for contest1, users_in_contest in field.items():
    print(f"{contest1}: {len(users_in_contest)} participants")
    nums = 1
    for ring1, ring_score1 in ring_scores:
        if ring1[1] == contest1:
            print(f"{nums}. {ring1[0]} <::> {ring_score1}")
            nums += 1

print("Individual standings:")
individuals = sorted(individuals.items(), key=lambda x: (-x[1], x[0]))
numbering = 1
for user, individual_standing in individuals:
    print(f"{numbering}. {user} -> {individual_standing}")
    numbering += 1