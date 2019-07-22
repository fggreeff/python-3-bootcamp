import unittest

import utils.syntax_helper


class SyntaxHelperTestCase(unittest.TestCase):

    def test_cap_text_one_word(self):
        '''This test asserts that one word is capitalized'''
        input_text = 'python'
        result = syntax_helper.cap_text(input_text)
        self.assertEqual(result, 'Python')

    def test_cap_text_multiple_words(self):
        '''This test asserts that multiple words are capitalized'''
        input_text = 'python is cool'
        result = syntax_helper.cap_text(input_text)
        self.assertEqual(result, 'Python is cool')


if __name__ == "__main__":
    unittest.main()
