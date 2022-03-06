with open('text.txt', 'r') as file:
    replacements = {"-", ",", ".", "!", "?"}
    idx = 0
    while True:
        line = file.readline().strip()
        if not line:
            break
        if idx % 2 == 1:
            idx += 1
            continue
        for symbol in replacements:
            line = line.replace(symbol, '@')
        idx += 1
        reversed_line = line.split()[::-1]
        print(' '.join(reversed_line))