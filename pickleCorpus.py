import nltk
import pickle
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import PunktWordTokenizer
from nltk.collocations import *

# TODO generate corpus from text files 
# tokenizer = RegexpTokenizer("[\w']+")

new_corpus = PlaintextCorpusReader('corpus/', '.*', word_tokenizer= PunktWordTokenizer())
corpus = nltk.Text(new_corpus.words())
all_bigrams = nltk.bigrams(corpus) # get a list of all the bigrams in the corpus
cond_freq_dist = nltk.ConditionalFreqDist(all_bigrams) # TPs for all bigrams as a dict
fileName = "pickledCorpus"
fileObject = open(fileName, 'wb')
pickle.dump(cond_freq_dist, fileObject)
fileObject.close()
