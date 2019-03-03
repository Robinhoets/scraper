# main file for scraping a website


#--- IMPORTS ---

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup



#--- DEFINITIONS ---

def connect():
	"""
	takes no arguments.
	returns boolean value of whether attempt to get url was successful.
	"""
	url = 'http://www.google.com'
	response = get_url(url)
	if response is not None:
		return True	#.......change this to return list........
	
	return False

def get_url(url):
	"""
	takes http url as argument.
	returns content of response from def is_good_response.
	"""
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
	takes url stream as argument.
	Returns True if the response seems to be HTML, False otherwise.
  	"""
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200 
		and content_type is not None 
		and content_type.find('html') > -1)


def print_error(e):
	"""
	takes in request exception as argument.
	prints exception message to terminal.
	"""
	print(e)

get_heading():
	"""

	"""

	
#--- MAIN METHOD ---

if __name__=='__main__':
	print('Connecting to the website')
	
	is_connected = connect()
	print('is connected: ' +str(is_connected))

	if(is_connected)
		get_heading()
	else:
		print("Not connected... Exiting...)












