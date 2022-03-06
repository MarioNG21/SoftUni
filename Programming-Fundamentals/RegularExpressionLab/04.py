import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()

valid_nums = re.finditer(pattern, text)

valid_num = (num.group() for num in valid_nums)

print(*valid_num)