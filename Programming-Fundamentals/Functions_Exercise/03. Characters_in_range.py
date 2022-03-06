def chr_in_range(chr_1: str, chr_2: str):
    chr_1_int = ord(chr_1)
    chr_2_int = ord(chr_2)
    charackter = ""
    for digits in range(chr_1_int + 1, chr_2_int):
        digits_str = chr(digits)
        charackter += digits_str
    return charackter


chr_one = input()
chr_two = input()
print(*chr_in_range(chr_one, chr_two))
