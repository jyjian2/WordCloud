import unittest, os
from src.wordcloud import WordCloud

class TestWordCloud(unittest.TestCase):
    def test_load(self):
        wc = WordCloud('test/test-paragraph01.txt')
        wc.load()
        self.assertEqual(wc.sorted_word_tuples[0], ('pig', 4))
        self.assertEqual(wc.sorted_word_tuples[1], ('a', 3))

    def test_toImage(self):
        wc = WordCloud('test/test-paragraph00.txt')
        wc.load()
        wc.toImage()
        self.assertTrue(os.path.exists(wc.image_path))

if __name__ == '__main__':
    unittest.main()
