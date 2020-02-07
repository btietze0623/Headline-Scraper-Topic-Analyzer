import pandas as pd
import re, string, unicodedata
import nltk
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
#from articles import articles

#update the below file name for whatever data file you want to analyze
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

print(stem_and_lemmatize(['run', 'ran', 'running']))

#tokenize and normalize (lower case) all the headlines
headline_tokenized = []
for i in headline_list:
  headline_lower = i.lower()
  headline_remove = headline_lower.replace('|', '')
  headline_remove2 = headline_remove.replace('$', '')
  headline_remove3 = headline_remove2.replace('.', '')
  headline_stripped = headline_remove3.strip()
  headline_tokenized.append(nltk.word_tokenize(headline_stripped))

#build a giant list into a list of all individual words used
headline_pre_lem = []
for i in headline_tokenized:
  for j in i:
    headline_pre_lem.append(j)

print(headline_pre_lem)

#now lemmatize
headline_lemmatized = lemmatize_verbs(headline_pre_lem)
print(headline_lemmatized)

# Update stop_list:
stop_list = [";","the","&","amp","apos","to","be","a","in","of"," ","s","and",":","for","on","  ","'s","as","have","with","from","at","after","us","will","his","new","'","it","that"]
# filtering topics for stop words
def filter_out_stop_words(corpus):
  no_stops_corpus = []
  for chapter in corpus:
    no_stops_chapter = " ".join([word for word in chapter.split(" ") if word not in stop_list])
    no_stops_corpus.append(no_stops_chapter)
  return no_stops_corpus

filtered_for_stops = filter_out_stop_words(headline_lemmatized)

#Run bag of words analysis to see most highly cited words
wordfreq = {}
for token in filtered_for_stops:
    if token not in wordfreq.keys():
        wordfreq[token] = 1
    else:
        wordfreq[token] += 1

#Count most frequent uses
from collections import Counter
k = Counter(wordfreq) 
high = k.most_common(20)
print(high)
print("Dictionary with 20 highest values:") 
print("Keys: Values") 
  
for i in high: 
    print(i[0]," :",i[1]," ")   
