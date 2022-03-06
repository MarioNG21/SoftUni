sublists = input().split('|')

result = []


for idx in range(len(sublists) - 1,  -1, -1):
    element = sublists[idx].split()
    result += element


print(' '.join(result))
