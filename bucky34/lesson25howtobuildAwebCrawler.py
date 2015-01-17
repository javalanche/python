#could not get this program to work
#TODO: research urllib and BeautifulSoup4 to get this working
import urllib
from bs4 import BeautifulSoup

def cl_spider(max_pages):
    page = 100
    while page < max_pages:
	url = 'http://dallas.craigslist.org/search/w4m?s=' + str(page)
	source_code = urllib.get(url)
	print(str(source_code))
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for link in soup.findAll('a', {'class': 'hdrlnk'}):
	    href = link.get('href')
	    print(href)
	page +=100

cl_spider(100)

    
