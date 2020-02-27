#!/usr/bin/env python3

class WordCloud:

    def __init__(self, filename):
        self.filename = filename

    def load(self):
        wrd_freq_dict = {}
        infile = open(self.filename, "r")
        wrds = infile.read()
        for w in wrds:
            if w not in wrd_freq_dict:
                wrd_freq_dict[w] = 0
            else:
                wrd_freq_dict[w] += 1
        return wrd_freq_dict


wc = WordCloud("test.txt")
wc.load()
