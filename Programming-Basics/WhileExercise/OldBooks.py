the_book = input()
name_of_other_books = ""
times = 0
while name_of_other_books != "No More Books":
    name_of_other_books = input()
    if name_of_other_books == the_book or name_of_other_books == "No More Books":
        break
    times += 1

if name_of_other_books == the_book:
    print(f"You checked {times} books and found it.")

else:
    print("The book you search is not here!")
    print(f"You checked {times} books.")