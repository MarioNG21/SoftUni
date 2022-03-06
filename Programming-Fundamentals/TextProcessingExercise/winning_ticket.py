tickets = [t.strip() for t in input().split(", ") if not t.isspace()]

winning_symbol_1 = "@" * 6
winning_symbol_2 = "#" * 6
winning_symbol_3 = "$" * 6
winning_symbol_4 = "^" * 6
for ticket in tickets:
    length = len(ticket)
    if length != 20:
        print("invalid ticket")
        continue

    left_part = ticket[:10]
    right_part = ticket[10:]
    match_symbol = ''

    if winning_symbol_1 in left_part and winning_symbol_1 in right_part:
        match_symbol = "@"
    elif winning_symbol_2 in left_part and winning_symbol_2 in right_part:
        match_symbol = "#"
    elif winning_symbol_3 in left_part and winning_symbol_3 in right_part:
        match_symbol = "$"
    elif winning_symbol_4 in left_part and winning_symbol_4 in right_part:
        match_symbol = "^"
    else:
        print(f'ticket "{ticket}" - no match')
        continue

    left_matches = left_part.count(match_symbol)
    right_matches = right_part.count(match_symbol)

    min_matches = min(left_matches, right_matches)

    if min_matches == 10:
        print(f'ticket "{ticket}" - {min_matches}{match_symbol} Jackpot!')
    else:
        print(f'ticket "{ticket}" - {min_matches}{match_symbol}')