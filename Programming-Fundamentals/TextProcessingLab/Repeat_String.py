words = input().split()

results = ''
for word in words:
    results += word * len(word)

print(results)



