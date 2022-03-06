start_number = int(input())
end_number = int(input())
units_start = start_number % 10
tens_start = start_number % 100 // 10
hundred_start = start_number % 1000 // 100
thousands_start = start_number // 1000
units_end = end_number % 10
tens_end = end_number % 100 // 10
hundred_end = end_number % 1000 // 100
thousands_end = end_number // 1000
for thousands in range(thousands_start, thousands_end+1):
    for hundred in range(hundred_start, hundred_end+1):
        for tens in range(tens_start, tens_end+1):
            for unit in range(units_start, units_end+1):
                if unit % 2 == 1 and tens % 2 == 1 and hundred % 2 == 1 and thousands % 2 == 1:
                    print(f"{thousands}{hundred}{tens}{unit}", end=" ")
