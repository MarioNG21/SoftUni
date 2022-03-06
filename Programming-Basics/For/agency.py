# броя продадени билети за възрастни
# броя продадени билети за деца
#  Нетната цена за възрастен се определя от авиокоманията
#  детският билет е 70 процента по евтин
# към получената цена(детски + възрастни) + такса обслужване
# крайната печалба на авиокомпанията е 20 процента от получената цена
name_airline = input()
tickets_for_adults = int(input())
amount_tickets_for_kids = int(input())
net_price_for_adults = float(input())
additional_price = float(input())

net_price_for_kids = net_price_for_adults - (0.7 * net_price_for_adults)
net_price_for_kids_with_net = net_price_for_kids + additional_price
net_price_for_adults_with_net = net_price_for_adults + additional_price
whole_price_adults = round(net_price_for_adults_with_net * tickets_for_adults, 2)
whole_price_kids = round(net_price_for_kids_with_net * amount_tickets_for_kids, 2)
price = whole_price_adults + whole_price_kids

airline_income = price * 0.2
print(f"The profit of your agency from {name_airline} tickets is {airline_income:.2f} lv.")