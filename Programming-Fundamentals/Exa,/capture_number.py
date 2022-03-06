import re
patter = r"\d+"
text = input()
matches = []
while True:
    match_numbers = re.findall(patter, text)
    if not match_numbers == []:
        for el in match_numbers:
            match_num = int(el)
            print(int(match_num), end=' ')
    text = input()
