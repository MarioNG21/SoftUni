file_name = input().split('\\')

file_name_and_extension = file_name[len(file_name)-1].split(".")
print(f"File name: {file_name_and_extension[0]}")
print(f"File extension: {file_name_and_extension[1]}")
