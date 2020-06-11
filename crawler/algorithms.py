import pandas as pd
import re
import requests

from bs4 import BeautifulSoup
from time import sleep,localtime,strftime

class Crawler:
	"""
	"""
	__header = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}
	def __init__(self, url, sarcasm, as_archived=False, file_name=""):
		self.__url = url
		self.__sarcasm = sarcasm
		self.__as_archived = as_archived
		self.__file_name = file_name

		self.__htmls = []
		self.__pages = None
		self.__raw_data = []
		self.__dataframe = pd.DataFrame(columns=["article_link","headline","is_sarcastic","text"])


	def get_one_request(self, page_url):
		"""Get one html request.

		Returns
		-------
		requests.models.Response
			Request related to a specific page.
		"""
		error = None

		while error != False:
			error = False
			try:
				html = requests.get(page_url, headers=self.__header)
			except requests.RequestException:
				print("([!] Error occurred, trying again the page {0} after 5 seconds".format(page_url))
				sleep(5)
				error = True
		return html


	def set_pages(self, html_class, re_string, start, end, element="a", shorter=0):
		"""Find the last page of a website.
		e.g. "Pages 1, 2, ..., 34, 35" <- Last page here is 35;
		Or find the strings rellated to the archived data.
		e.g. "News by year: 2020, 2019, ...,2005" <- Here is a list[2020, ..., 2005].
		
		In both cases it'll depend if the __as_archived variable is True or False.

		Parameters
		----------
		html_class : str
			Class of the a href attribute related to the maximum number.
		re_string : raw str
			Regular expression to find the last page refer.
		rm_start : int
			How much to exclude from the beginning of the substring founded by the RE.
		rm_end : int
			How much to exclude from the end of the substring founded by the RE.
		element: str, default "a"
			Element of the HTML to be founded.
		shorter: int, default 0
			If it's archived style page, set how much to remove from the url to get the
			pages url list. If necessary.
		"""
		find_pages = re.compile(re_string)
		html = True

		while html == True:
			html = self.get_one_request(self.__url + ("1", "")[self.__as_archived])
		bs = BeautifulSoup(html.text, "html.parser")
		element = str(bs.find_all(element, class_=html_class))

		if self.__as_archived == True:
			pages = []
			for archive in find_pages.finditer(element):
				pages.append(str(self.__url[:-shorter]) + element[archive.start()+start:archive.end()-end])
		else:
			for page in find_pages.finditer(element):
				pages = int(element[page.start()+start:page.end()-end])

		self.__pages = pages


	def get_html_requests(self):
		htmls = []
		"""Get all requests from a ammount of URLs.

		Returns
		-------
		list
			All pages requested.

		Note
		----
		May occurs an infinite loop if any type of internet interference happens.
		"""
		print("[+] Requesting all pages (it might take a while) from:\n\t\'{0}\'".format(self.__url))

		if self.__as_archived == True:
			for arch in self.__pages:
				htmls.append(self.get_one_request(arch))
		else:
			for page_num in range(1, self.__pages):
				page_url = self.__url + str(page_num)
				htmls.append(self.get_one_request(page_url))
				
		return htmls


	def set_raw_data(self, html_class, re_string, element="div"):
		"""Find some specific part of an HTML class.

		Parameters
		----------
		html_class : str
			Class of the a specified element.
		re_element : str
			Regular expression to find a specific HTML element.
		element : str, default "div"
			Element of the HTML to be founded.
		"""
		find_element = re.compile(re_string)

		for html in self.get_html_requests():
			bs = BeautifulSoup(html.text, "html.parser")
			raw = str(bs.find_all(element, class_=html_class))
			for text in find_element.finditer(raw):
				self.__raw_data.append(raw[text.start():text.end()])

		print("[+] Total of {0} raw data collected".format(len(self.__raw_data)))


	def set_data_frame(self, re_link, re_title, rm_start, rm_end, url_prefix=""):
		"""Find a specific data of links and title information from a list of
		HTML specific data.

		Parameters
		----------
		re_link : str
			Regular expression to find a href HTML element.
		re_title : str
			Regular expression to find a title HTML element.
		rm_start : tuple, (int,int)
			How much to exclude from the beginning of two substrings founded by the
			two regular expressions: re_link and re_title, in that order.
		rm_end : tuple, (int,int)
			How much to exclude from the end of two substrings founded by the two
			regular expressions: re_link and re_title, in that order.
		url : str, default ""
			A substring to add in the beginning of the link founded by the re_link;
			It's only used if the website URL is different from the original used in
			the crawling.
		"""
		find_link = re.compile(re_link)
		find_title = re.compile(re_title)

		for data in self.__raw_data:
			data_list = [[],[],[],[]]
			for tmp in find_link.finditer(data):
				data_list[0] = url_prefix + data[tmp.start()+rm_start[0]:tmp.end()+rm_end[0]]
			for tmp in find_title.finditer(data):
				data_list[1] = data[tmp.start()+rm_start[1]:tmp.end()+rm_end[1]]
			if data_list[1] == "" or data_list[3] == "":
				continue
			data_list[2] = self.__sarcasm
			self.__dataframe.loc[len(self.__dataframe)] = data_list

		print("[+] Dataframe completed")


	def get_dataframe(self):
		return self.__dataframe