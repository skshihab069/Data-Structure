# check a word if its palindrome or not
def palindrome(word):
    return word[::-1] == word


Word = input("Please enter a string : ")
print(palindrome(Word))
