import nltk
import pickle
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import PunktWordTokenizer
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
from string import punctuation

# read all files in the corpus
new_corpus = PlaintextCorpusReader('fullLettersOfNote/', '.*\.txt', word_tokenizer= PunktWordTokenizer())
# get all words
corpus = nltk.Text(new_corpus.words())
#remove random punctuation from corpus
common_punct = "!?,;:'" #punctuation we want to keep
unwanted_punct = [p for p in punctuation if p not in common_punct] # what we want to get rid of
cleaned_corpus = [word for word in corpus if word not in unwanted_punct] # ditch the weird punctuation
all_bigrams = [bigram for bigram in nltk.bigrams(cleaned_corpus)] # get a list of all the bigrams in the corpus from the bigram generator
#get frequencies of bigrams 
bigram_freqs = nltk.FreqDist(all_bigrams)
kept_bigrams = [bigram for bigram in all_bigrams if bigram_freqs[bigram] >2]

cond_freq_dist = nltk.ConditionalFreqDist(kept_bigrams) # TPs for all bigrams as a dict
fileName = "pickledCorpus"
fileObject = open(fileName, 'wb')
pickle.dump(cond_freq_dist, fileObject) #pickle corpus
fileObject.close()
