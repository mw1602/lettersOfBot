import nltk
import pickle
import numpy as np
from nltk.tokenize import regexp_tokenize

# freq_dict = pickle.load('pickledCorpus')

start_words = ["I", 'You', 'We', 'Hello', 'Dear', 'They'] #TODO do we want to allow for a greater range of start words?
end_words = ['.','?','!','...']

def loadPickledCorpus(path):
	pkl_file = open(path, 'rb')
	cfd = pickle.load(pkl_file)
	pkl_file.close()

def chooseStartWord(start_words):
	return np.random.choice(start_words, 1)

def build_sentence(start, end_words, cfd):
	if start in end_words:
		return start
	next_word = getNextWord(start, cfd)
	sentence = start + ' ' + build_sentence(next_word, end_words, cfd) #TODO handle spaces with punctuation?
	return sentence

def getNextWord(word, cfd):
	if len(cfd[word]) != 0: #to deal with words that have no continuations. Just end the sentence here for now. 
		word_dict = cfd[word]
		words = word_dict.keys()
		freqs = word_dict.values()
		normed_freqs = [float(f)/sum(freqs) for f in freqs]
		next_word = np.random.choice(words, 1,p=normed_freqs)
		return next_word[0]
	else: return '.'
