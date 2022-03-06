number_of_groups = int(input())
whole_members = 0
first_group = 0
second_group = 0
third_group = 0
fourth_group = 0
fifth_group = 0
for groups in range(1, number_of_groups+1):
    members = int(input())
    whole_members += members
    if members <= 5:
        first_group += members
    elif 6 <= members <= 12:
        second_group += members
    elif 13 <= members <= 25:
       third_group += members
    elif 26 <= members <= 40:
        fourth_group += members
    elif members >= 41:
        fifth_group += members

first_group_in_percent = (first_group / whole_members) * 100
second_group_in_percent = (second_group / whole_members) * 100
third_group_in_percent = (third_group / whole_members) * 100
fourth_group_in_percent = (fourth_group / whole_members) * 100
fifth_group_in_percent = (fifth_group / whole_members) * 100

print(f"{first_group_in_percent:.2f}%")
print(f"{second_group_in_percent:.2f}%")
print(f"{third_group_in_percent:.2f}%")
print(f"{fourth_group_in_percent:.2f}%")
print(f"{fifth_group_in_percent:.2f}%")