#TODO: I believe this stuff has changed in python34 so will need to review all of the older python first
import urllib2
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = urllib2.Request.get_full_url(url).text
    print(source_code)
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class':'post-title'}):
        content = post_text.string
	words = content.lower().split()
	
    
