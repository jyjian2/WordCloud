#!/usr/bin/env python3

class WordCloud:

    def __init__(self, filename):
        self.filename = filename
        self.sorted_word_tuples = []

    def load(self):
        wrd_freq_dict = {}
        infile = open(self.filename, "r")
        wrds = infile.read()
        wrd = wrds.split()
        for w in wrd:
            if w not in wrd_freq_dict:
                wrd_freq_dict[w] = 1
            else:
                wrd_freq_dict[w] += 1
        wrd_freq_tup = [(k, v) for k, v in wrd_freq_dict.items()]
        self.sorted_word_tuples = sorted(wrd_freq_tup, key=lambda e: e[1], reverse=True)



wc = WordCloud("test/test-paragraph.txt")
wc.load()
print(wc.sorted_word_tuples)
