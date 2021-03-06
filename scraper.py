# main file for scraping a website


#--- IMPORTS ---

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup



#--- DEFINITIONS ---

def connect(user_url):
	"""
	takes no arguments.
	returns boolean value of whether attempt to get url was successful.
	"""
	url = user_url
	response = get_url(url)
	if response is not None:
		headings = get_headings(response)
		return headings

	raise Exception('Error: cannot retrieve contents at {}'.format(url))

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

def get_headings(response):
	"""
	takes in url streams content.
	returns list of hedings.
	"""
	soup = BeautifulSoup(response, 'html.parser')
	headings = set()
	for p in soup.select('p'):
		for heading in p.text.split('\n'):
			if len(heading) > 0:
				headings.add(heading.strip())
	return list(headings)

def print_ps(heading_list):
	"""
	takes in a list of headings collected.
	prints list to screen.
	"""
	for x in range(len(heading_list)):
		y=x+1
		print("Paragraph %d:   " %y + heading_list[x] + "\n")




#--- MAIN METHOD ---

if __name__=='__main__':
	
	url = input("Enter a web address: ")
	print('Connecting to the website')
	
	heading_list = connect(url)
	print('is connected...')
	
	print_ps(heading_list)
	











