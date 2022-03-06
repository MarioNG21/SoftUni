import re
pattern = r"(?P<Day>\d{2})(?P<separator>([-/\.]))(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

text = input()

valid_dates = re.finditer(pattern, text)

for data in valid_dates:
    current_date = data.groupdict()
    print(f"Day: {current_date['Day']}, Month: {current_date['Month']}, Year: {current_date['year']}")
