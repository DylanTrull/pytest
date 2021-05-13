import unittest
import palindrome

class TestPalindrome(unittest.TestCase):
    def test_False(self):
        self.assertFalse(palindrome.isPalindrome("franks"))
    def test_ActuallyFalse(self):
        self.assertTrue(palindrome.isPalindrome("Dylan"))
    def test_True(self):
        self.assertTrue(palindrome.isPalindrome("frankssknarf"))
    def test_cap(self):
        self.assertEqual(palindrome.isPalindrome("ss"),palindrome.isPalindrome("SS"))


if __name__ == '__main__':
    unittest.main()
