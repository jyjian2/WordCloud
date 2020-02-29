#!/usr/bin/env python3
import sys
import string
from PIL import Image, ImageDraw, ImageFont

class WordCloud:

    def __init__(self, filename):
        self.filename = filename
        self.sorted_word_tuples = []

    def load(self):
        string.punctuation
        wrd_freq_dict = {}
        infile = open(self.filename, "r")
        file_str = infile.read()
        infile.close()
        for w in file_str.split():
            for p in string.punctuation:
                w = w.replace(p, '')
            if w not in wrd_freq_dict:
                wrd_freq_dict[w] = 1
            else:
                wrd_freq_dict[w] += 1

        wrd_freq_tup = [(k, v) for k, v in wrd_freq_dict.items()]
        self.sorted_word_tuples = sorted(wrd_freq_tup, key=lambda e: e[1], reverse=True)

    def toImage(self):
        self.image_path = 'test.png'
        img = Image.new('RGB', (600, 600), color = 'white')
        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', size=50)
        d.text((300,300), 'Helloxxx', font=fnt, fill=(148,0,211))
        img.save(self.image_path)


if __name__ == "__main__":
    wc = WordCloud(sys.argv[1])
    wc.load()
    wc.toImage()
