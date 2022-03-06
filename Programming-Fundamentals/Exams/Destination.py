import re
pattern = r"(?P<separator>(\=|\/))(?P<destination>([A-Z][A-Za-z]{2,}))(?P=separator)"
text = input()

matches = re.finditer(pattern, text)
travel_points = 0
destinations = []
for match in matches:
    destination = match.group("destination")
    travel_points += len(destination)
    destinations.append(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")

