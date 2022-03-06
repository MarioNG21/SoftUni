words = input().split()
searched_word = input()

palindromes_list = [el for el in words if el == el[::-1]]
print(palindromes_list)
print(f"Found palindrome {palindromes_list.count(searched_word)} times")