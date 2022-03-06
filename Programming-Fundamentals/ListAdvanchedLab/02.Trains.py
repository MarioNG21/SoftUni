wagons = int(input())

train = [0] * wagons # умножаваме нулите по броя на вагоните

command = input()
while command != "End":
    data = command.split()
    if data[0] == "add":
        train[-1] += int(data[1])
    elif data[0] == "insert":
        index = int(data[1])
        n_people = int(data[2])
        train[index] += int(n_people)
    elif data[0] == "leave":
        index = int(data[1])
        n_people = int(data[2])
        train[index] -= int(n_people)
    command = input()
print(train)