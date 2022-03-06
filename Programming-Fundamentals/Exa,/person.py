number = int(input())
if number <= 0:
    exit()
for i in range(number):
    name_age = input().split()
    first_name = ""
    first_age = 0
    for ch in range(len(name_age)):
        new_ch = name_age[ch]
        start_index = 0
        if "@" in new_ch or "#" in new_ch:
            for _ in range(len(new_ch)):
                el = new_ch[_]
                if el == "@":
                    start_index = int(_)
                    name = new_ch[(start_index+1):len(new_ch)-1]
                    first_name += name
                    break
                elif el == "#":
                    new_index = _
                    age = new_ch[(new_index+1):len(new_ch)-1]
                    first_age += int(age)
                    break
    print(f"{first_name} is {first_age} years old.")
