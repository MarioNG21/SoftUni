company_info = {}

command = input()
while command != "End":
    cmd_info = command.split("-> ")
    company_name = cmd_info[0]
    employee_id = cmd_info[1]

    if company_name not in company_info.keys():
        company_info[company_name] = []

    if employee_id not in company_info[company_name]:
        company_info[company_name].append(employee_id)

    command = input()
new_list_sorted = sorted(company_info.items(), key=lambda kvp: kvp[0])

for company_name, employee_id in new_list_sorted:
    print(company_name)
    for emp_id in employee_id:
        print(f"-- {emp_id}")