# a test file 4 palindrome:

import unittest

from palindrome1 import palindrome

# palindrome() 

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome('racecar'), True)
        self.assertEqual(palindrome('palindrome'), False)
        self.assertEqual(palindrome('amanaplanacanalpanama'), True)
        self.assertEqual(palindrome('aa'), False)
        self.assertEqual(palindrome('dad'), True)
        self.assertEqual(palindrome('b'), False)



if __name__ == '__main__':
    unittest.main() 