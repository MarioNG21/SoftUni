number = int(input())
word_dict = {}
for i in range(number):
    word = input()
    synonym = input()
    if word not in word_dict:
        word_dict[word] = []
    word_dict[word].append(synonym)

for key, value in word_dict.items():
    print(f"{key} - {', '.join(value)}")