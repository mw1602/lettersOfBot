import nltk
import pickle
import numpy as np
from nltk.tokenize import regexp_tokenize

# freq_dict = pickle.load('pickledCorpus')

start_word = "I"
end_words = ['.','?','!','...',',']
# corpus = nltk.book.text1
# # tokenizer = RegexpTokenizer("[\w]+([-'][\w]+)*]")
# tokens= regexp_tokenize(corpus,"[\w']+")

# tokens = tokenizer.tokenize(corpus)

# bigrams = nltk.bigrams(corpus)
# cfd = nltk.ConditionalFreqDist(bigrams)


def build_sentence(start, end_words, cfd):
	if start in end_words:
		return start
	next_word = getNextWord(start, cfd)
	sentence = start + ' ' + build_sentence(next_word, end_words, cfd)
	return sentence


def getNextWord(word, cfd):
	word_dict = cfd[word]
	words = word_dict.keys()
	freqs = word_dict.values()
	normed_freqs = [float(f)/sum(freqs) for f in freqs]
	next_word = np.random.choice(words, 1,p=normed_freqs)
	return next_word[0]
