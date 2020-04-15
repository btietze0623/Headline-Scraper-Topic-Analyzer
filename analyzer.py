import pandas as pd
import re, string, unicodedata, nltk
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
from nltk.util import ngrams
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_csv("CombinedHeadlines.csv")
print(df.shape)

#importCSV
import csv
r = csv.reader(open("CombinedHeadlines.csv")) # Here your csv file
lines = list(r)
#Now I have nested lists

#create 1 list with all the headlines
headline_list = []
for i in lines:
  headline_list.append(i[0])

#stem and lemmatize function
def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def stem_and_lemmatize(words):
    stems = stem_words(words)
    lemmas = lemmatize_verbs(words)
    return lemmas

#tokenize and normalize (lower case) all the headlines
headline_tokenized = []
for i in headline_list:
  headline_lower = i.lower()
  headline_remove = headline_lower.replace('|', '')
  headline_remove2 = headline_remove.replace('$', '')
  headline_remove3 = headline_remove2.replace('.', '')
  headline_stripped = headline_remove3.strip()
  headline_tokenized.append(nltk.word_tokenize(headline_stripped))

#Build a list of all words used
headline_pre_lem = []
for i in headline_tokenized:
  for j in i:
    headline_pre_lem.append(j)

#now lemmatize
headline_lemmatized = lemmatize_verbs(headline_pre_lem)

# Update stop_list:
stop_list = [";","an", "a","the","&","amp","apos","to","be","a","in","of"," ","s","and",":","for","on","  ","'s","as","have","with","from","at","after","us","will","his","new","'","it","that"]
# filtering topics for stop words
list_filtered = []

for w in headline_lemmatized:
    if w not in stop_list:
        list_filtered.append(w)

clean_data_set = list_filtered

#run ngram analysis (n of 1 is bag of words analysis)
ngram_n = 3
print_line_ngram = "n-gram analysis: n of {}".format(ngram_n)
print(print_line_ngram)
ngram_list = ngrams(clean_data_set,ngram_n)
print(ngram_list)
print(Counter(ngram_list).most_common(20))
