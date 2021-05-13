import palindrome
import pytest

def test_is_palindrome():
    assert palindrome.isPalindrome("Nick") == False

def test_PalindromeCaps():
    assert palindrome.isPalindrome("DylanNalyD") == True  #shows that I didnt test for cap sensitivity

def test_palindromeTrue():
    assert palindrome.isPalindrome("DylannalyD") == True
