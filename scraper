from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#get_time_and_date
from datetime import datetime, date
now = datetime.now()
current_time = str(now.strftime("%H:%M:%S"))
today = date.today()

#FoxNews
fox_url = 'https://www.foxnews.com/'

#opening up connecction, grabbing the page
urlClient = uReq(fox_url)
page_html = urlClient.read()
urlClient.close()
#to find the html...page_html


#html parser
page_soup = soup(page_html, "html.parser")

#grab containers sub bullets
containers = page_soup.findAll("li",{"class":"related-item title-color-default"})
len(containers)
#grab containers main stories
headline_containers = page_soup.findAll("h2",{"class":"title title-color-default"})
len(headline_containers)
#container = containers[0]
#full_title_container = page_soup.findAll("a",{"class":"item-title"})

filename = "CombinedHeadlines.csv"
f = open(filename, "w")

#subbullets
for container in containers:
	headline_default = container.a.text
	headline_default_strip = headline_default.strip()
	url = container.a["href"]
	outlet = 'Fox News'

	print("headline: " + headline_default)
	print(url)
	print(today)
	print(current_time)

	f.write(headline_default_strip.replace(",", "|") + "," + str(url) + "," + str(today) +  "," + str(current_time) + "," + outlet + "\n")

#main stories
for container in headline_containers:
	headline_default = container.a.text
	headline_default_strip = headline_default.strip()
	headline_update = headline_default_strip.replace("‚Äô",'')
	url = container.a["href"]
	outlet = 'Fox News'

	print("headline: " + headline_default)
	print(url)
	print(today)
	print(current_time)

	f.write(headline_update.replace(",", "|") + "," + str(url) + "," + str(today) +  "," + str(current_time) + "," + outlet + "\n")

#ABCNews
abc_url = 'https://abcnews.go.com/'

#opening up connecction, grabbing the page
urlClient = uReq(abc_url)
page_html = urlClient.read()
urlClient.close()
#to find the html...page_html


#html parser
page_soup = soup(page_html, "html.parser")

#grab containers
containers = page_soup.findAll("div",{"class":"headlines-li-div"})
len(containers)
#container = containers[0]
#full_title_container = page_soup.findAll("a",{"class":"item-title"})


for container in containers:
	headline_default = container.a.text
	headline_update = headline_default.replace("‚Äô",'')
	url = container.a["href"]
	outlet = 'ABC News'

	print("headline: " + headline_default)
	print(url)
	print(today)
	print(current_time)

	f.write(headline_update.replace(",", "|") + "," + str(url) + "," + str(today) +  "," + str(current_time) + "," + outlet +  "\n")

#CNN

cnn_url = 'https://www.cnn.com/sitemaps/cnn/news.xml'

#opening up connecction, grabbing the page
urlClient = uReq(cnn_url)
page_xml = urlClient.read()
urlClient.close()
#to find the xml...page_xml


#xml parser
page_soup = soup(page_xml, "xml")

#grab containers
containers = page_soup.findAll("news:title")
len(containers)
#container = containers[0]
#full_title_container = page_soup.findAll("a",{"class":"item-title"})


for container in containers:
	headline_default = str(container)
	headline_update1 = headline_default.strip('<news:title>')
	headline_update2 = headline_update1.strip('</')	
	headline_update3 = headline_update2.replace("&amp;apos;",'\'')
	headline_update3 = headline_update2.replace("‚Äô",'')
	#url = container["href"]
	outlet = 'CNN'

	print("headline: " + headline_update3)
	#print(url)
	print(today)
	print(current_time)

	f.write(str(headline_update3.replace(",", "|")) + "," + "," + str(today) +  "," + str(current_time) + "," + outlet + "\n")

#BusinessInsider
bi_url = 'https://www.businessinsider.com/'

#opening up connecction, grabbing the page
urlClient = uReq(bi_url)
page_html = urlClient.read()
urlClient.close()
#to find the html...page_html


#html parser
page_soup = soup(page_html, "html.parser")

#grab containers
containers = page_soup.findAll("a",{"class":"tout-title-link"})
len(containers)
#container = containers[0]
#full_title_container = page_soup.findAll("a",{"class":"item-title"})

for container in containers:
	headline_default = container.text
	headline_default1 = headline_default.strip()
	url = container["href"]
	outlet = 'Business Insider'

	print("headline: " + headline_default1)
	print(url)
	print(today)
	print(current_time)

	f.write(headline_default1.replace(",", "|") + "," + str(url) + "," + str(today) +  "," + str(current_time) + "," + outlet + "\n")

f.close()
