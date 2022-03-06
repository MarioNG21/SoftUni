command = input()
company_dict = {}
while not command == "End":
    company_name, emp_id = command.split("-> ")
    if company_name not in company_dict:
        company_dict[company_name] = []

    if emp_id not in company_dict[company_name]:
        company_dict[company_name].append(emp_id)

    command = input()

sorted_dict = sorted(company_dict.items(), key=lambda kvp: kvp[0])

for company, employee in sorted_dict:
    print(company)
    for i in employee:
        print(f"-- {i}")