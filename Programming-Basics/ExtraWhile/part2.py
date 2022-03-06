funds_needed = int(input())
funds_collected = 0
command = input()
payments_count = 0
paid_by_cash = 0
total_paid_by_cash = 0
paid_by_card = 0
total_paid_by_card = 0
is_collected = False
while command != "End":
    product_price = int(command)
    payments_count += 1
    if payments_count % 2 == 0:
        if product_price >= 10:
            paid_by_card += 1
            total_paid_by_card += product_price
            funds_collected += product_price
            print('Product sold!')
        else:
            print('Error in transaction!')
    else:
        if product_price <= 100:
            paid_by_cash += 1
            total_paid_by_cash += product_price
            funds_collected += product_price
            print('Product sold!')
        else:
            print('Error in transaction!')
    if funds_collected >= funds_needed:
        is_collected = True
        break
    command = input()
if is_collected:
    average_by_cash = total_paid_by_cash / paid_by_cash
    average_by_card = total_paid_by_card / paid_by_card
    print(f'Average CS: {average_by_cash:.2f}')
    print(f'Average CC: {average_by_card:.2f}')
else:
    print('Failed to collect required money for charity.')