file = open('reading_files_readline_demos.py', 'r')
x = 5

# while True:
#     text = file.readline()
#     print(text)
#     print('------')
#     if not text:
#         break


while True:
    # reads at most 7 characters on the line
    text = file.readline(7)
    print(text)
    print('------')
    if not text:
        break