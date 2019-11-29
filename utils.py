import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_book_info_from_isbn(isbn):
	URL = 'http://opac.nlc.cn/F/'

	headers = {
		'Host': 'opac.nlc.cn',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
	}

	params = {'find_base': ['NLC01', 'NLC09'],
	 'func': ['find-m'],
	 'find_code': ['ISB'],
	 'request': [str(isbn)],
	 'filter_code_1': ['WLN'],
	 'filter_code_2': ['WYR'],
	 'filter_code_3': ['WYR'],
	 'filter_code_4': ['WFM'],
	 'filter_code_5': ['WSL']}

	# fix all bugs with try..except
	try:
		page = requests.get(URL, headers=headers, params=params)
		soup = BeautifulSoup(page.content.decode('utf8'), 'lxml')

		table = str(soup.find('div', class_='tabcontent', id='details2').find('table'))
		table = pd.read_html(table)[0]
		info = dict(zip(table.iloc[:, 0], table.iloc[:, 1]))
		return info
	except:
		return None
