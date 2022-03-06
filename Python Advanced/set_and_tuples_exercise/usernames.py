usernames = set()

counter = int(input())

for _ in range(counter):
    username = input()
    usernames.add(username)

[print(x) for x in usernames]
