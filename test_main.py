import unittest
from main import letter_counter, words_counter


class TestTextAnalysis(unittest.TestCase):
    def test_words_counter(self):
        """Test the words_count function"""
        self.assertEqual(words_counter("Hello world"), 2)
        self.assertEqual(words_counter(""), 0)

    def test_letter_counter(self):
        """Test the letter_count function"""
        self.assertEqual(letter_counter("Hello"), {'h':1,
                                                   'e':1,
                                                   'l':2,
                                                   'o':1})
        self.assertEqual(letter_counter("AaBb"),{'a': 2,
                                                 'b': 2} )
        self.assertEqual(letter_counter("1,@!#$%^&*() -"), {})


if __name__ == "__main__":
    unittest.main()