file = open('text.txt', 'r')

counter = 0
replacements = {"-", ",", ".", "!", "?"}

for f in file:
    if counter % 2 == 0:
