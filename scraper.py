# main file for scraping a website

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def connect():
	url = 'http://www.google.com'
	response = get_url(url)
	if response is not None:
		return True
	
	return False

def get_url(url):
	try:
		with closing(get(url, stream=True)) as response:
			if is_good_response(response):
				return response.content
			else:
				return None

	except RequestException as e:
		print_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def print_error(e):
    print(e)

if __name__=='__main__':
	print('Connecting to the website')
	
	is_connected = connect()
	print('is connected: ' +str(is_connected))
