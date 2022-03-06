tail = input()
body = input()
head = input()

zoo = [head, body, tail]
zoo[0], zoo[2] = zoo[2], zoo[0]
print(zoo)