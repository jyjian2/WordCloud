import unittest, os
from src.wordcloud import WordCloud

class TestWordCloud(unittest.TestCase):
    def test_load(self):
        wc = WordCloud('test/test-paragraph01.txt')
        wc.load()
        self.assertEqual(wc.sorted_word_tuples[0], ('pig', 4))
        self.assertEqual(wc.sorted_word_tuples[1], ('apple', 3))

    def test_read_stop_words(self):
        wc = WordCloud('test/test-paragraph00.txt')
        self.assertEqual(len(wc.stop_words), 204)
        self.assertEqual(wc.stop_words[0], 'a')

    def test_toImage(self):
        wc = WordCloud('test/test-paragraph00.txt')
        wc.load()
        wc.toImage()
        self.assertTrue(os.path.exists(wc.image_path))



if __name__ == '__main__':
    unittest.main()
