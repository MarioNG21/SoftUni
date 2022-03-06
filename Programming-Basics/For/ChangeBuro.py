# 1 биктойн - 1168
# 1 юоана - 0.15
# 1 долар 1.76 лева
# 1 евро = 1.95 лева
# от 0 до 5 комисионна от крайната сметка

bitcoins = int(input())
chinese_money = float(input())
commission = float(input())

from_bitcoin_to_euro = (bitcoins * 1168) / 1.95
from_chinese_money_to_euro = ((chinese_money * 0.15) * 1.76) / 1.95
euro = from_chinese_money_to_euro + from_bitcoin_to_euro
euro_with_commission = euro - (commission/100) * euro
print(f"{euro_with_commission:.2f}")