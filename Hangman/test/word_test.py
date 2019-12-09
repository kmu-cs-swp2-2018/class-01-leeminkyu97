import unittest
import os
import string
from word import Word


class WordTest(unittest.TestCase):

    def setUp(self):
        self.word = Word(os.path.normpath(
            os.path.join(os.path.dirname(__file__), '../words.txt')))

    def test_get_word(self):
        assert self.word is not None

    def test_words_count(self):
        self.assertEqual(len(self.word.words), 19184)

    def test_get_guessed_characters(self):
        self.assertIsInstance(self.word.get_guessed_characters(), set)

    def test_guess(self):
        for char in string.ascii_lowercase:
            result = self.word.guess(char)
            if result == 1:
                self.assertEqual(self.word.current_status,
                                 self.word.get_word())
            elif result is not None:
                self.assertEqual(result, -1)

        self.assertEqual(len(self.word.get_guessed_characters()), 26)


if __name__ == '__main__':
    unittest.main()