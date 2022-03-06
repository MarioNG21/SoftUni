number = float(input())
positivity = ""
size = ""
if number == 0:
    positivity = "zero"
elif number > 0:
    positivity = "positive"
    if abs(number) >= 1 and abs(number) > 1000000:
        size = "large"
    elif abs(number) >= 1:
        size = ""
    else:
        size = "small"
else:
    positivity = "negative"
    if abs(number) >= 1 and abs(number) > 1000000:
        size = "large"
    elif abs(number) >= 1:
        size = ""
    else:
        size = "small"
print(f"{size} {positivity}")