def isPalindrome(word):
    return word == word[::-1]


word = (input("Enter a word: "))
answer = isPalindrome(word)

if (answer == True):
    print(word + " is a palindrome")
else:
    print(word + " isn't a palindrome")
