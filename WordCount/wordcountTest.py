import unittest
import wordcount


class TestWordCount(unittest.TestCase):
    def test_Equals(self):
        self.assertEqual(wordcount.wordCount("the quick brown fox jumps over the bridge"), 8)
    def test_NotEqual(self):
        self.assertNotEqual(wordcount.wordCount("the quick brown fox jumps over the bridge"), 8)
    def test_NotNull(self):
        self.assertIsNotNone(wordcount.wordCount("the quick brown fox jumps over the bridge"))
    def test_Spaces(self):
        self.assertEqual(wordcount.wordCount("thequickbrownfoxjumpsoverthebridge"), wordcount.wordCount("yes"))

if __name__ == '__main__':
    unittest.main()
