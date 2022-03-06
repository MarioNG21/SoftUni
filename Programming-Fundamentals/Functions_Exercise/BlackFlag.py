days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

def mission_completed(days: int, amount: int, awaiting_plunder: float):
    sum = 0
    for day in range(1, days+1):
        sum += amount
        if day % 3 == 0:
            sum += 0.5 * amount
        if day % 5 == 0:
            sum -= 0.3 * sum

    if sum >= awaiting_plunder:
        return f"Ahoy! {sum:.2f} plunder gained."
    else:
        return f"Collected only {(sum/awaiting_plunder)*100:.2f}% of the plunder."


print(mission_completed(days_of_plunder, daily_plunder, expected_plunder))