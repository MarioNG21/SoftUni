from math import floor
import re
text = input()
pattern = r"(?P<separator>(\#|\|))(?P<item>([A-Za-z\s])+)(?P=separator)(?P<date>([0-9]{2}/[0-9]{2}/[0-9]{2}))(?P=separator)(?P<calories>([0-9]+))(?P=separator)"

cal_per_day = 2000

matches = re.finditer(pattern, text)

sum_cal = [(int(i.group("calories"))) for i in matches]
sum_caloires = 0
for i in sum_cal:
    sum_caloires += i
days = floor(sum_caloires / cal_per_day)
print(f"You have food to last you for: {days} days!")
matches = re.finditer(pattern, text)
for match in matches:
    name = match.group("item")
    date = match.group("date")
    calories = match.group("calories")
    print(f"Item: {name}, Best before: {date}, Nutrition: {calories}")