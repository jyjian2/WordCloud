test:
	python3 src/wordcloud.py test/test-paragraph.txt
	python3 src/wordcloud.py test/test-paragraph01.txt

.PHONY:test
