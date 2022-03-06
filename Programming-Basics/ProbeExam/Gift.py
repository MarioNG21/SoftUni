pocket_money = float(input())
income_per_day = float(input())
expenses_for_5_days = float(input())
gift_price = float(input())

pocket_money_for_whole_period = pocket_money * 5
income_for_whole_period = income_per_day * 5
whole_sum = pocket_money_for_whole_period + income_for_whole_period
whole_sum -= expenses_for_5_days

if whole_sum >= gift_price:
    print(f"Profit: {whole_sum:.2f} BGN, the gift has been purchased.")
else:
    diff = gift_price - whole_sum
    print(f"Insufficient money: {diff:.2f} BGN.")