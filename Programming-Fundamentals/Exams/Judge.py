command = input()

contest_dict = {}

personal_records = {}

while not command == "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in contest_dict:
        contest_dict[contest] = {username: [points]}

    elif username in contest_dict[contest]:
        contest_dict[contest][username].append(points)

    elif username not in contest_dict[contest]:
        contest_dict[contest][username] = [points]

    command = input()


for u, items in contest_dict.items():
    print(f"{u}: {len(items)} participants")
    ind = 1

    for i, j in sorted(items.items(), key=lambda x: (-max(x[1]), x[0])):
        print(f"{ind}. {i} <::> {max(j)}")
        ind += 1

        if i not in personal_records:
            personal_records[i] = 0
        personal_records[i] += max(j)

counter = 1
print("Individual standings:")
for person, own_score in sorted(personal_records.items(), key=lambda x: (-x[1], x[0])):
    print(f"{counter}. {person} -> {own_score}")
    counter += 1