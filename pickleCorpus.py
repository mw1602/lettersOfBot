import nltk
import pickle
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import PunktWordTokenizer
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()

# read all files in the corpus
new_corpus = PlaintextCorpusReader('fullLettersOfNote/', '.*\.txt', word_tokenizer= PunktWordTokenizer())
# get all words
corpus = nltk.Text(new_corpus.words())
all_bigrams = nltk.bigrams(corpus) # get a list of all the bigrams in the corpus
#get frequencies of bigrams 
bigram_freqs = nltk.FreqDist(all_bigrams)
kept_bigrams = [k for k,v in bigram_freqs.items() if v > 1]

cond_freq_dist = nltk.ConditionalFreqDist(kept_bigrams) # TPs for all bigrams as a dict
fileName = "pickledCorpus"
fileObject = open(fileName, 'wb')
pickle.dump(cond_freq_dist, fileObject) #pickle corpus
fileObject.close()
