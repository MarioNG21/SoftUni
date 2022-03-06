s = 'I love Python'

stack = []

for i in s:
    stack.append(i)

result = ''
while len(stack) > 0:
    result += stack.pop()

print(result)