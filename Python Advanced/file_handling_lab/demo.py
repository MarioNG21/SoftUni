file = open('demo.py', 'r')

while True:
    text = file.read(1)
    print(text)
    if not text:
        break