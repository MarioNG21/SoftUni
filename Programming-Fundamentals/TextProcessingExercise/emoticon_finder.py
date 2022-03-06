text = input().split()

for _ in range(0, len(text)):
    ch = text[_]
    if ":" in ch:
        new_ch = ch[1]
        print(f":{new_ch}")