def calculation(operation, num_1, num_2):
    if operation == "multiply":
        return num_1 * num_2
    elif operation == "divide":
        return num_1 // num_2
    elif operation == "add":
        return num_1+num_2
    elif operation == "subtract":
        return num_1 - num_2

oper = input()
number_1 = int(input())
number_2 = int(input())

print(calculation(oper, number_1, number_2))