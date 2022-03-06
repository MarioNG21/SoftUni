period = input()
type_contract = input()
mobile_net = input()
months = int(input())
whole_price = 0
if type_contract == "Small":
    if period == "one":
        price_month = 9.98
        if mobile_net == "yes":
            if price_month <= 10:
                price_month += 5.5
            elif 10 < price_month <= 30:
                price_month += 4.35
            elif price_month > 30:
                price_month += 3.85
            whole_price = price_month * months
        else:
            whole_price = price_month * months
    elif period == "two":
        price_month = 8.58
        if mobile_net == "yes":
            if price_month <= 10:
                price_month += 5.5
            elif 10 < price_month <= 30:
                price_month += 4.35
            elif price_month > 30:
                price_month += 3.85
            whole_price = price_month * months
        else:
            whole_price = price_month * months
        if period == "two":
            whole_price = whole_price - 0.0375 * whole_price
elif type_contract == "Middle":
    if period == "one":
        price_month = 18.99
        if mobile_net == "yes":
            if price_month <= 10:
                price_month += 5.5
            elif 10 < price_month <= 30:
                price_month += 4.35
            elif price_month > 30:
                price_month += 3.85
            whole_price = price_month * months
        else:
            whole_price = price_month * months
    elif period == "two":
        price_month = 17.09
        if mobile_net == "yes":
            if price_month <= 10:
                price_month += 5.5
            elif 10 < price_month <= 30:
                price_month += 4.35
            elif price_month > 30:
                price_month += 3.85
            whole_price = price_month * months
        else:
            whole_price = price_month * months
        if period == "two":
            whole_price = whole_price - 0.0375 * whole_price
elif type_contract == "Large":
    if period == "one":
        price_month = 25.98
        if mobile_net == "yes":
            if price_month <= 10:
                price_month += 5.5
            elif 10 < price_month <= 30:
                price_month += 4.35
            elif price_month > 30:
                price_month += 3.85
            whole_price = price_month * months
        else:
            whole_price = price_month * months
    elif period == "two":
        price_month = 23.59
        if mobile_net == "yes":
            if price_month <= 10:
                price_month += 5.5
            elif 10 < price_month <= 30:
                price_month += 4.35
            elif price_month > 30:
                price_month += 3.85
            whole_price = price_month * months
        else:
            whole_price = price_month * months
        if period == "two":
            whole_price = whole_price - 0.0375 * whole_price
elif type_contract == "ExtraLarge":
    if period == "one":
        price_month = 35.99
        if mobile_net == "yes":
            if price_month <= 10:
                price_month += 5.5
            elif 10 < price_month <= 30:
                price_month += 4.35
            elif price_month > 30:
                price_month += 3.85
            whole_price = price_month * months
        else:
            whole_price = price_month * months
    elif period == "two":
        price_month = 31.79
        if mobile_net == "yes":
            if price_month <= 10:
                price_month += 5.5
            elif 10 < price_month <= 30:
                price_month += 4.35
            elif price_month > 30:
                price_month += 3.85
            whole_price = price_month * months
        else:
            whole_price = price_month * months
        if period == "two":
            whole_price = whole_price - 0.0375 * whole_price
print(f"{whole_price:.2f} lv.")