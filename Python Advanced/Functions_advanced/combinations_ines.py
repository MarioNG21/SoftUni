def combination(names, count, current_names = []):
    if len(current_names) == count:
        print(', '.join(current_names))
        return
    for i in range(len(names)):
        current_names.append(names[i])
        combination(names[i+1:], count, current_names)
        current_names.pop()



names = input().split(', ')
count = int(input())
combination(names, count)
