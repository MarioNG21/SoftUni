money_needed = float(input())
money_on_hand = float(input())
spend_counter = 0
total_counter = 0
sum = money_on_hand
while True:
    action = input()
    money = float(input())
    total_counter +=1
    if action == "spend":
        spend_counter += 1
        if sum >= money:
            sum = sum - money
        else:
            sum = 0
    if spend_counter == 5:
        print ("You can't save the money.")
        print (f"{total_counter}")
        break
    elif action == "save":
        spend_counter = 0
        sum = sum + money
    if sum >= money_needed:
        print (f"You saved the money for {total_counter} days.")
        break