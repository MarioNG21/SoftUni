word = input().split()
word_dict = {}

for _ in range(len(word)):
    ch = word[_]
    for el in range(len(ch)):
        el = ch[el]
        if el not in word_dict:
            word_dict[el] = 1
        elif el in word_dict:
            word_dict[el] += 1


for key,value in word_dict.items():
    print(f"{key} -> {value}")