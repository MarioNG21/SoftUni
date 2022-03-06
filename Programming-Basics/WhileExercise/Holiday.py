needed_money = float(input())
current_money = float(input())
count_spend_days = 0    # броя на дни в които харчим
count_days = 0 # брой на дни в които или пестим или харчим
while current_money < needed_money:
    # извършвам действие (spend or save)
    action = input()
    count_days += 1
    made_money = float(input())
    if action == "spend":
        current_money -= made_money
        if current_money < 0:
            current_money = 0
        count_spend_days += 1

        if count_spend_days == 5:
            print("You can't save the money.")
            print(f"{count_days}")
            break
    elif action == "save":
        current_money += made_money
        count_spend_days = 0


else:
    print(f"You saved the money for {count_days} days.")