def write_to_file(file_path, mode, text):
    file = open(file_path, mode)
    file.write(text)
    file.close()


write_to_file('files/numbers.txt', 'a', '''0
1
2
3
4
5
6'''
)

write_to_file('files/numbers.txt', 'a', '''New 
Text
''')