# main file for scraping a website

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def connect():
	url = 'http://www.google.com'
	response = simple_get(url)
	if response is not None:
		return true
	
	return false


if __name__=='__main__':
	print('Connecting to the website')
	
	is_connected = connect()
	print('is connected: ' +str(is_connected))
