import re
patter = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
names = input()

matches = re.findall(patter, names)
print(' '.join(matches))