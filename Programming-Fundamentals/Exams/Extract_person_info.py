number_of_times = int(input())
start_index = 0
end_index = 0
star_index_age = 0
end_index_age = 0
name = ''
for i in range(number_of_times):
    new_message = input()
    if "@" in new_message:
        index = new_message.index("@")
        start_index = index
    if "|" in new_message:
        end_index = new_message.index("|")

    if "#" in new_message:
        star_index_age = new_message.index("#")
    if "*" in new_message:
        end_index_age = new_message.index("*")
    name = new_message[start_index+1: end_index]
    age = new_message[star_index_age + 1: end_index_age]
    print(f"{name} is {int(age)} years old.")