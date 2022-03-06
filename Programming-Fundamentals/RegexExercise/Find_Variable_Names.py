import re
text = input()

pattern = r"\b\_(?P<variable_name>([A-Za-z]+|\d+))\b"

variable = re.finditer(pattern, text)
variable_name = [word.group() for word in variable]

print(','.join(variable_name))