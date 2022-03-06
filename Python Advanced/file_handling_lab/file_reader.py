file = open('file_reader.py', 'r')
x = 5

i = 1
for line in file.readlines():
    print(f"{i}: {line}")
    i += 1
