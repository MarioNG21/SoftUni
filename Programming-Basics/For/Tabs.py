tabs_count = int(input())
salary = int(input())


#  за всеки таб -> име на сайт -> проверка на сайта
#  ако е един от забранените -> намаля заплатата
#  ако останем без заплата -> свършва програмата

for tab in range(1, tabs_count + 1):
    site_name = input()
    if site_name == "Facebook":
        salary -= 150
    elif site_name == "Instagram":
        salary -= 100
    elif site_name == "Reddit":
        salary -= 50
    if salary <= 0:
        print(f"You have lost your salary.")
        break
if salary > 0:
    print(salary)