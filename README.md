# News-Scraper-Topic-Analyzer

Use case: Many of today's news sources are biased. You might frequently see some topics shown on CNN that are not covered on Fox News and sometimes even vice versa. The purpose of this tool is to quickly pull the key topics that are being discussed overall across varying news sources. 

These 2 programs 1) Scraper.py scrapes news sources CNN, Business Insider, Fox, and ABC and creates a central datasource of that moment's headlines and 2) Analyzer.py normalizes and lemmatizes the data and runs an ngram analysis to identify the key topics of the day

Below you can see that I'm reading in the CombinedHeadlines.csv document which is the combined headlines created from the Scraper.py script. 

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
