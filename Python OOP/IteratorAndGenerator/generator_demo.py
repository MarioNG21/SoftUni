def custom_range(start, end):
    for x in range(start, end):
        yield x


iter1 = custom_range(1, 15)
for x in custom_range(1, 15):
    print(x)
    
