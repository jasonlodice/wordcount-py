#!/usr/bin/python3

import string
import sys
from itertools import groupby

"""Design Notes

The goal of this design is to minimize how much of the file must be held in memory
at any one time.  The file is read line by line, and at any one time, only two
Word instances are referenced.
"""


class Word:
    """A class to encapsulate a string word and character counting behavior."""

    def __init__(self):
        self.val = ""
        self._cached_max_char_freq = None

    def append(self, ch):
        """Append character to the word"""
        self.val += ch

        #   invalidate cached value
        self._cached_max_char_freq = None

    def value(self):
        return self.val

    def max_char_freq(self):
        """Return count of most frequently occurring non-punctuation character."""

        #   cached for performance
        if not self._cached_max_char_freq:
            #   tuple of char, count
            winner = ()

            #   lower case, strip punctuation
            data = self.val.lower().translate(str.maketrans("", "", string.punctuation))

            #   group by sorted characters in the string
            for key, group in groupby(sorted(data), lambda x: x):
                #   find count in char group
                count = len(list(group))
                #   replace winner if count is greater than current winner
                if not winner or winner[1] < count:
                    winner = (key, count)

            # if no winner, return 0
            self._cached_max_char_freq = 0 if not winner else winner[1]

        return self._cached_max_char_freq


class WordBuilder:
    """Class which processes characters into Words"""

    def __init__(self):
        self._current_word = None

    def push_char(self, ch):

        if self._is_word_started() and WordBuilder._is_word_separator(ch):
            #   a word has been completed, return it
            word = self._current_word
            self._end_word()
            return word
        elif WordBuilder._is_allowed_char(ch):
            #   add character to the current word
            if not self._is_word_started():
                self._start_word()

            self._current_word.append(ch)

        #   word was not completed
        return None

    def _is_word_started(self):
        return self._current_word is not None

    def _start_word(self):
        self._current_word = Word()
        return

    def _end_word(self):
        self._current_word = None

    @staticmethod
    def _is_allowed_char(ch):
        return str.isalpha(ch) or ch == '\'' or ch == '-'

    @staticmethod
    def _is_word_separator(ch):
        return not WordBuilder._is_allowed_char(ch) and (str.isspace(ch) or (ch in string.punctuation))


def main():
    """Main method executes when script is run stand alone"""
    try:
        word_builder = WordBuilder()

        found_word = None

        #   if no file path specified, exit
        if len(sys.argv) < 2:
            return

        # open file read only
        file = open(sys.argv[1], "r")

        for line in file:
            for ch in line:
                #   pass each character one at a time
                word = word_builder.push_char(ch)

                #   if word was created, see if it should become new found_word
                if word:
                    if not found_word or word.max_char_freq() > found_word.max_char_freq():
                        found_word = word

        #   print the word
        if found_word:
            print(found_word.value())
    except:
        #   suppress all errors
        pass

if __name__ == "__main__":
    main()
