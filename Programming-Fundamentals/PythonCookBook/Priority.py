items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
new = items[a]
s = 'HelloWorld'
a.indices(len(s))
for i in range(*new.indices(len(s))):
    print(s[i])