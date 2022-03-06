usernames = input().split(", ")
valid = []
for user in usernames:
    length = len(user)
    if 3 <= length <= 16:
        if user.isalnum() or "-" in user or "_" in user:
            if user.strip() or user.rstrip() or user.lstrip():
                valid.append(user)

for _ in valid:
    print(_)