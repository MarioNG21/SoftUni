import re

pattern = r"(?P<surr>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=surr)"
text = input()
pattern_number = r"\d"
match_number_as_strings = re.findall(pattern_number, text)
all_nums_as_int = [int(num) for num in match_number_as_strings]

threshold = 1
for el in all_nums_as_int:
    threshold *= el

emojis_to_print = []
emoji_matches = re.finditer(pattern, text)
print(f'Cool threshold: {threshold}')

emoji_count = 0

for match in re.finditer(pattern, text):
    emoji_count += 1
    data = match.groupdict()
    emoji = data["emoji"]
    emoji_coolness = sum([ord(letter) for letter in emoji])
    if emoji_coolness >= threshold:
        emojis_to_print.append(f"{data['surr']}{data['emoji']}{data['surr']}")

print(f"{emoji_count} emojis found in the text. The cool ones are:")
#print('\n'.join(emojis_to_print))
for i in emojis_to_print:
    print(i)