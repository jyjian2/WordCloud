import unittest
from src.wordcloud import WordCloud

class TestWordCloud(unittest.TestCase):
    def test_load(self):
        wc = WordCloud('test/test-paragraph01.txt')
        wc.load()
        self.assertEqual(wc.sorted_word_tuples[0], ('pig', 4))

if __name__ == '__main__':
    unittest.main()
