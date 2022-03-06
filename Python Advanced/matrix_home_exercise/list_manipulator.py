from collections import deque


def list_manipulator(ll: list, *args):
    result = deque(ll)
    if len(args) > 0:
        first_command = args[0]
        second_command = args[1]
        if len(args) >= 3:
            if first_command == "add":
                if second_command == "beginning":
                    for num in args[2:][::-1]:
                        result.appendleft(num)
                elif second_command == "end":
                    for num in args[2:]:
                        result.append(num)

            elif first_command == "remove":
                for num in args[2:]:
                    if second_command == "beginning":
                        for i in range(num):
                            result.popleft()
                    elif second_command == "end":
                        for i in range(num):
                            result.pop()
        else:
            if first_command == "remove":
                    if second_command == "beginning":
                        result.popleft()
                    elif second_command == "end":
                        result.pop()
        ll = []
        for el in result:
            ll.append(el)
        return ll

    else:
        return ll


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

