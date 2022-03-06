from collections import deque

substring = deque(input().split())

main_colours = {'red', 'yellow', 'blue'}
secondary_colours = {'orange', 'purple', 'green'}


collected_colours = []
while substring:
    left = substring.popleft()
    right = substring.pop() if substring else ""
    color = left + right
    if color in main_colours or color in secondary_colours:
        collected_colours.append(color)
        continue
    color = right + left
    if color in main_colours or color in secondary_colours:
        collected_colours.append(color)
    else:
        left = left[:-1]
        right = right[:-1]
        if left:
            substring.insert(len(substring) // 2, left)
        if right:
            substring.insert(len(substring) // 2, right)
secondary_required_colours = {
    'orange': ["red", "yellow"],
    'purple': ["red", "blue"],
    'green': ["blue", "yellow"]
}

for color in collected_colours:
    if color in main_colours:
        continue
    required_colours = secondary_required_colours[color]
    is_valid = all([x in collected_colours for x in required_colours])
    if not is_valid:
        collected_colours.remove(color)

print(collected_colours)