#!/usr/bin/python3

import unittest
from word_count import Word

class WordTest(unittest.TestCase):
    def test_all_freq_one_returns_one(self):
        word = Word()
        word.append('h')
        word.append('i')

        self.assertEqual(1, word.max_char_freq())

    def test_freq_two_returns_two(self):
        word = Word()
        word.append('h')
        word.append('e')
        word.append('l')
        word.append('l')
        word.append('o')

        self.assertEqual(2, word.max_char_freq())

    def test_ignore_case(self):
        word = Word()
        word.append('h')
        word.append('e')
        word.append('l')
        word.append('L')
        word.append('o')

        self.assertEqual(2, word.max_char_freq())

    def test_ignore_non_letters_two(self):
        word = Word()
        word.append('-')
        word.append('\'')

        self.assertEqual(0, word.max_char_freq())

if __name__ == '__main__':
    unittest.main()
