needed_exp = float(input())
count_of_battles = int(input())

counter = 0
has_won = False
sum_of_exp = 0
for battle in range(1, count_of_battles + 1):
    exp_per_battle = float(input())
    counter += 1
    sum_of_exp += exp_per_battle
    if battle % 3 == 0:
        add_exp = 0.15 * exp_per_battle
        sum_of_exp += add_exp
    if battle % 5 == 0:
        less_exp = 0.10 * exp_per_battle
        sum_of_exp -= less_exp
    if battle % 15 == 0:
        add_exp = 0.05 * exp_per_battle
        sum_of_exp += add_exp
    if sum_of_exp >= needed_exp:
        has_won = True
        break

if has_won == True:
    print(f"Player successfully collected his needed experience for {counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {(needed_exp - sum_of_exp):.2f} more needed.")
