file_path = 'my_first_file.txt'
content = 'I just created my first file'

file = open(file_path, 'w')
file.write(content)
file.close()
