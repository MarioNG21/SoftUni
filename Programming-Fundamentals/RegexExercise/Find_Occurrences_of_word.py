import re
# правим го за да бъдат case insensitve
text = input().lower()
word = input().lower()

pattern = rf'\b{word}\b'

word_count = len(re.findall(pattern, text))
print(word_count)