start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
is_found = False
for first in range(start, end+1):
    for second in range(start, end+1):
        counter += 1
        if magic_number == first + second:
            is_found = True
            print(f"Combination N:{counter} ({first} + {second} = {magic_number})")
    if is_found == True:
        break
if is_found == False:
   print(f"{counter} combinations - neither equals {magic_number}")