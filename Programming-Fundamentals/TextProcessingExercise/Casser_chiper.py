text = input()
encrypted_list = ''.join([chr(ord(ch)+3) for ch in text])
print(encrypted_list)