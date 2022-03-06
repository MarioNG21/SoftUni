import re
text = input()
pattern = r"(?P<separator>(\@|\#))([A-Za-z]{3,})(?P=separator)(?P=separator)([a-zA-Z]{3,})(?P=separator)"
mirror_words = []

matches = re.finditer(pattern, text)
count = 0
for match in matches:
    count += 1
    word = match.group(3)
    mirror_word = match.group(4)
    mirror_word_reversed = mirror_word[::-1]

    if word == mirror_word_reversed:
        mirror_words.append(f"{word} <=> {mirror_word}")

if count == 0:
    print("No word pairs found!")
else:
    print(f"{count} word pairs found!")


if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))