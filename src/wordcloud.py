#!/usr/bin/env python3
import sys
import string
from PIL import Image, ImageDraw, ImageFont
import random

class WordCloud:

    def __init__(self, filename):
        self.filename = filename
        self.sorted_word_tuples = []
        self.read_stop_words()

    def read_stop_words(self):
        file = open("src/stop_words.txt", "r")
        self.stop_words = file.read().split('\n')
        file.close()

    def load(self):
        string.punctuation
        wrd_freq_dict = {}
        infile = open(self.filename, "r")
        file_str = infile.read()
        infile.close()
        for w in file_str.split():
            for p in string.punctuation:
                w = w.replace(p, '')
            if w in self.stop_words:
                continue
            elif w not in wrd_freq_dict:
                wrd_freq_dict[w] = 1
            else:
                wrd_freq_dict[w] += 1

        wrd_freq_tup = [(k, v) for k, v in wrd_freq_dict.items()]
        self.sorted_word_tuples = sorted(wrd_freq_tup, key=lambda e: e[1], reverse=True)

    def toImage(self):
        self.image_path = 'test.png'
        img = Image.new('RGB', (600, 600), color = 'white')
        d = ImageDraw.Draw(img)
        sum_freq = 0
        for text in self.sorted_word_tuples:
            sum_freq += int(text[1])
        for text in self.sorted_word_tuples:
            x = random.randrange(50,550)
            y = random.randrange(50,550)
            sz = int((text[1] / sum_freq) * 3600)
            fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', sz)
            d.text((x,y), text[0], font=fnt, fill=(148,0,211))
        img.save(self.image_path)


if __name__ == "__main__":
    wc = WordCloud(sys.argv[1])
    wc.load()
    wc.toImage()
