from urllib.request import urlopen
from IPython import embed
from bs4 import BeautifulSoup
import re

call_info = "http://gsd-auth-callinfo.s3-website.us-east-2.amazonaws.com/"
page = urlopen(call_info)
parsed_page = BeautifulSoup(page)

#area codes
area_codes = parsed_page.find_all('a', href=re.compile('AreaCode'))
for code in area_codes:
	print(code.contents[0].split('area code')[0])

#phone numbers
phone_numbers = parsed_page.find_all('a', href=re.compile('Phone'))
for number in phone_numbers:
	print(number.contents[0])	

#number of comments
number_of_comments = parsed_page.find_all('span', class_='postCount')
for number in number_of_comments: 
	print(number.contents[0])

#comments
comments = parsed_page.find_all('div', class_='oos_previewBody')
for comment in comments: 
	print(comment.contents[0])

