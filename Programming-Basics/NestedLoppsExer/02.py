n = int(input())
for thousands in range(1, 10):
    for hundreds in range(1, 10):
        for tens in range(1, 10):
            for units in range(1, 10):
                check1 = n % units == 0
                check2 = n % tens == 0
                check3 = n % hundreds == 0
                check4 = n % hundreds == 0
                if check1 and check2 and check3 and check4:
                    print(f"{thousands}{hundreds}{tens}{units}", end="")