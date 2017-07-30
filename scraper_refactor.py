from urllib.request import urlopen
from IPython import embed
from bs4 import BeautifulSoup
import re

class Scraper(object):

	def __init__(self):
		call_info = "http://gsd-auth-callinfo.s3-website.us-east-2.amazonaws.com/"
		page = urlopen(call_info)
		self.parsed_page = BeautifulSoup(page)

	def get_area_codes(self):
		area_codes = Scraper().parsed_page.find_all('a', href=re.compile('AreaCode'))
		codes = []
		for code in area_codes:
			codes.append(code.contents[0].split('area code')[0])

	def get_phone_numbers(self):
		phone_numbers = Scraper().parsed_page.find_all('a', href=re.compile('Phone'))
		numbers = []
		for number in phone_numbers:
			numbers.append(number.contents[0])		

	def get_number_of_comments(self):
		number_of_comments = Scraper().parsed_page.find_all('span', class_='postCount')
		comment_numbers = []
		for number in number_of_comments:
			comment_number.append(number.contents[0])

	def get_all_comments(self):
		comments = Scraper().parsed_page.find_all('div', class_='oos_previewBody')
		all_comments = []
		for comment in comments: 
			all_comments_.append(comment.contents[0])	

	#def get_single_post_with_all_attributes(self):
		#get area_code, phone_number, number of comments and comment for single post
		#and return in best data structure for handoff to the DB