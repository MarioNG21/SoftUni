import heapq
empty_stack = []
counter = int(input())
for _ in range(counter):
    querie = input()
    if querie.startswith('1'):
        cmd_arg = querie.split()
        num = int(cmd_arg[1])
        empty_stack.append(num)
    elif querie.startswith('2'):
        if empty_stack:
            empty_stack.pop()
    elif querie.startswith('3'):
        largest = heapq.nlargest(1, empty_stack)
        print(*largest)
    elif querie.startswith('4'):
        smallest = heapq.nsmallest(1, empty_stack)
        print(*smallest)

last_stack = []
while len(empty_stack) > 0:
    new_el = empty_stack.pop()
    last_stack.append(str(new_el))
print(', '.join(last_stack))