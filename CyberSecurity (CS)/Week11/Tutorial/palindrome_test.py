import unittest
from functions import is_palindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome_word(self):
        word = "racecar"
        result = is_palindrome(word)
        self.assertTrue(result)

    def test_non_palindrome_word(self):
        word = "hello"
        result = is_palindrome(word)
        self.assertFalse(result)

    def test_palindrome_with_spaces(self):
        sentence = "a man a plan a canal panama"
        result = is_palindrome(sentence)
        self.assertTrue(result)
    
    def test_palindrome_with_uppercase(self):
        word = "Madam"
        result = is_palindrome(word)
        self.assertTrue(result)