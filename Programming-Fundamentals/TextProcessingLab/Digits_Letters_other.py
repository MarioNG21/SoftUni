sting = input()

digits = ""
letters = ""
characters = ""

for chr in sting:
    if chr.isdigit():
        digits += chr
    elif chr.isalpha():
        letters += chr
    else:
        characters += chr

print(digits)
print(letters)
print(characters)