# обем на басейн V -> цяло число
# дебит на първа траба P1 -> цяло число
# дебит на втора тръба P2 -> цяло число
# часове в които работника отсъства H -> реално число
#
#
sum_of_percent = 0

V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

sum_of_both_pipes_for_hour = P1 * H + P2 * H

if sum_of_both_pipes_for_hour <= V:
    sum_of_percent = (sum_of_both_pipes_for_hour / V) * 100
    pipe1 = ((P1 * H) / sum_of_both_pipes_for_hour) * 100
    pipe2 = ((P2 * H) / sum_of_both_pipes_for_hour) * 100
    print(f"The pool is {sum_of_percent:.2f}% full. Pipe 1: {pipe1:.2f}%. Pipe 2: {pipe2:.2f}%.")
elif sum_of_both_pipes_for_hour > V:
    more = (sum_of_both_pipes_for_hour - V)
    print(f"For {H:.2f} hours the pool overflows with {more:.2f} liters.")