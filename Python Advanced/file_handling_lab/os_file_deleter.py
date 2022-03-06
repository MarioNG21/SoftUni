import os
from os import path

# open('my_first_file.txt', 'w')
# print(path.exists('my_first_file.txt'))
#
# os.remove('my_first_file.txt')
#
# print(os.listdir('.'))


# for file_name in os.listdir():
#     full_path = path.join(
#         os.getcwd(),
#         file_name
#     )
#     print(full_path)
#
#     # to get absoluth path

ss = [os.getcwd()]

while ss:
    current_dir = ss.pop()
    print(current_dir)
    if path.isfile(current_dir):
        continue

    for file_path in os.listdir(current_dir):
        absolut_path = path.join(
            current_dir,
            file_path
        )
        ss.append(absolut_path)