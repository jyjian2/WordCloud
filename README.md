# WordCloud
Introduction
====================================
This project is to load a file and generate a image of words included.
The size of image is based on the frequancy of the word.
To run this file, you can follow the steps below:
1. open your terminal
2. Go to the file directory the file stored in.
3. use "python3 src/wordcloud.py test/test-paragraph00.txt"

manifest
=====================================
.
├── __init__.py (an empty file to make this project a python module)
├── Makefile (Makefile to automate the test process)
├── README.md
├── src
│   ├── __init__.py (an empty file to make this project a python module)
│   ├── stop_words.txt (words to ignore)
│   └── wordcloud.py (the main program)
└── test
    ├── __init__.py (an empty file to make this project a python module)
    ├── test-paragraph00.txt (text file for unit testing)
    ├── test-paragraph01.txt (test file for unit testing)
    └── test-wordcloud.py (test file for src/wordcloud.py)
