#!/usr/bin/python3

import unittest
from word_count import WordBuilder


class WordBuilderTest(unittest.TestCase):
    def setUp(self):
        self._word_builder = WordBuilder()

    def test_nonwhitespace_doesnot_return_word(self):
        word = self._word_builder.push_char('a')
        self.assertIsNone(word)

    def test_terminating_whitespace_returns_word(self):
        #   push non whitespace chars
        self._word_builder.push_char('h')
        self._word_builder.push_char('e')
        self._word_builder.push_char('l')
        self._word_builder.push_char('l')
        self._word_builder.push_char('o')

        #   whitespace should end a word
        word = self._word_builder.push_char(' ')

        self.assertIsNotNone(word)
        self.assertEqual("hello", word.value())

    def test_additional_whitespace_doesnot_return_word(self):
        #   push non whitespace chars
        self._word_builder.push_char('h')
        self._word_builder.push_char('e')
        self._word_builder.push_char('l')
        self._word_builder.push_char('l')
        self._word_builder.push_char('o')

        #   whitespace should end a word
        self._word_builder.push_char(' ')

        #   additional whitespace should not end a word
        word = self._word_builder.push_char(' ')

        self.assertIsNone(word)

    def test_hyphen_preserved_in_word(self):
        #   push non whitespace chars
        self._word_builder.push_char('B')
        self._word_builder.push_char('l')
        self._word_builder.push_char('u')
        self._word_builder.push_char('e')
        self._word_builder.push_char('-')
        self._word_builder.push_char('c')
        self._word_builder.push_char('o')
        self._word_builder.push_char('l')
        self._word_builder.push_char('l')
        self._word_builder.push_char('a')
        self._word_builder.push_char('r')

        #   whitespace should end a word
        word = self._word_builder.push_char(' ')

        self.assertIsNotNone(word)
        self.assertEqual("Blue-collar", word.value())

    def test_apostrophe_preserved_in_word(self):
        #   push non whitespace chars
        self._word_builder.push_char('w')
        self._word_builder.push_char('o')
        self._word_builder.push_char('n')
        self._word_builder.push_char('\'')
        self._word_builder.push_char('t')

        #   whitespace should end a word
        word = self._word_builder.push_char(' ')

        self.assertIsNotNone(word)
        self.assertEqual("won\'t", word.value())

if __name__ == '__main__':
    unittest.main()
