movie = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_for_ticket = float(input())
p_for_the_cinema = int(input())

income_from_tickets = number_of_tickets * price_for_ticket
whole_price = income_from_tickets * number_of_days
money_for_the_cinema = (p_for_the_cinema / 100 ) * whole_price
whole_price -= money_for_the_cinema
print(f"The profit from the movie {movie} is {whole_price:.2f} lv.")