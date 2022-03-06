# 20 procenta ot obshatata cena 3 prihoda na agenciqta
# netna cena na vuzrastni se opredelq ot kompaniqta , a na decata e 70 proceenta ot neq
agency_name = input()
number_of_adult_tickets = int(input())
number_of_kids_tickets = int(input())
adult_price_per_ticket = float(input())
tax = float(input())

adult_whole_price = number_of_adult_tickets * (adult_price_per_ticket+ tax)
kids_price_per_ticket = adult_price_per_ticket - 0.7 * adult_price_per_ticket
kids_whole_price = (kids_price_per_ticket + tax) * number_of_kids_tickets
whole_sum = adult_whole_price + kids_whole_price
agency_income = whole_sum * 0.20
print(f"The profit of your agency from {agency_name} tickets is {agency_income:.2f} lv.")