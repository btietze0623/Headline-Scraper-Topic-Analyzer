# News-Scraper-Topic-Analyzer

## Use case

Many of today's news sources are biased. You might frequently see some topics shown on CNN that are not covered on Fox News and sometimes even vice versa. The purpose of this tool is to quickly pull the key topics that are being discussed overall across varying news sources. 

These 2 programs 1) Scraper.py scrapes news sources CNN, Business Insider, Fox, and ABC and creates a central datasource of that moment's headlines and 2) Analyzer.py normalizes and lemmatizes the data and runs an ngram analysis to identify the key topics of the day

Below you can see that I'm reading in the CombinedHeadlines.csv document which is the combined headlines created from the Scraper.py script. 

```
df = pd.read_csv("CombinedHeadlines.csv")
print(df.shape)

#importCSV
import csv
r = csv.reader(open("CombinedHeadlines.csv")) # Here your csv file
lines = list(r)

#create 1 list with all the headlines
headline_list = []
for i in lines:
  headline_list.append(i[0])
```
## Preprocessing

Next I'm going to have to preprocess my list of headlines. I'm going to want to steam or lemmatize and normalize the headline list. In this case I have defined both stemming and lemmatization and a combined function, but I am only going to be using the lemmatizate function.

```
#stem and lemmatize functions
def stem_words(words):
    #Stem words in list of tokenized words
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    #Lemmatize verbs in list of tokenized words
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
```

Doing some sort of stemming or lemmatizing is critical because words may have different tenses (run, ran, running; car, care, caring) and I'm trying to convert all headlines into single words or topics so that I can eventually run a count to see which are most common in my dataset. Lemmatizing is usually more sophistocated than stemming. Take this example: If you stem the word 'Caring', it will return 'Car', which is incorrect. However, if you use lemmatizing, it will return 'care'.

Now I'm going to normalize my headlines, by stripping extra spaces, turning everything lowercase, making the words more uniform. I'm calling the lemmatize function here. I'm also including stop words here, which will exclude words or characters that I choose from the tokenized dataset. My final processed dataset is clean_data_set.

```
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

#Update stop_list:
stop_list = [";","an", "a","the","&","amp","apos","to","be","a","in","of"," ","s","and",":","for","on","  ","'s","as","have","with","from","at","after","us","will","his","new","'","it","that"]
#filtering topics for stop words
list_filtered = []

for w in headline_lemmatized:
    if w not in stop_list:
        list_filtered.append(w)

clean_data_set = list_filtered
```
## Topic analyis
Now I'm going to run my topic analysis, for which I am using an ngrams analysis. For this code, I have used an n of 3, and I am printing ou the top 20 results. This means that I will be returning 20 results of words that appear together in groups of 3. If I wanted to run a bag of words analysis where I wanted to return the top 20 single words that appear, I would set n = 1. I find for this data that n of 2 or 3 works best because it ignores filler words and shows greater context in the results.

```
#run ngram analysis (n of 1 is bag of words analysis)
ngram_n = 3
print_line_ngram = "n-gram analysis: n of {}".format(ngram_n)
print(print_line_ngram)
ngram_list = ngrams(clean_data_set,ngram_n)
print(ngram_list)
print(Counter(ngram_list).most_common(20))
```
