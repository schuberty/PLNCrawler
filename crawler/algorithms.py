import pandas as pd
import re
import requests

from bs4 import BeautifulSoup
from time import sleep,localtime

from crawler.requester import Requester

class Crawler:
	"""
	"""
	__header = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}
	def __init__(self, url, sarcasm, as_archived=False):
		self.__url = url
		self.__sarcasm = sarcasm
		self.__as_archived = as_archived

		self.__requests = list()
		self.__raw_data = list()
		self.__dataframe = pd.DataFrame(columns=["is_sarcastic","article_link","headline","text"])


	def set_requests(self, html_class, regex, remove, element="a", shorter=0):
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
		find_pages = re.compile(regex)
		urls = list()

		html = Requester.get_one_request(self.__url + ("1", "")[self.__as_archived])
		bs = BeautifulSoup(html.text, "html.parser")
		element = str(bs.find_all(element, class_=html_class))

		if self.__as_archived == True:
			for page in find_pages.finditer(element):
				urls.append(str(self.__url[:-shorter]) + element[page.start()+remove[0]:page.end()-remove[1]])
		else:
			for page in find_pages.finditer(element):
				pages = int(element[page.start()+remove[0]:page.end()-remove[1]]) + 1
			for page in range(1, pages):
				urls.append(self.__url + str(page))

		self.__requests = Requester(urls, 10).get_requests()


	def set_raw_data(self, html_class, regex, element="div"):
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
		find_element = re.compile(regex)

		for request in self.__requests:
			bs = BeautifulSoup(request.text, "html.parser")
			raw = str(bs.find_all(element, class_=html_class))
			for text in find_element.finditer(raw):
				self.__raw_data.append(raw[text.start():text.end()])

		print("[+] Total of {0:04d} raw data collected".format(len(self.__raw_data)))


	def set_data_frame(self, regex, remove, url_prefix=0):
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
		url_prefix int, default 0
			If there's anything to add in the begging of the url string to change in
			the columns of "link" in the dataset.
		"""
		find_link = re.compile(regex[0])
		find_title = re.compile(regex[1])

		for data in self.__raw_data:
			data_list = [[],[],[],[]]
			data_list[0] = self.__sarcasm
			for tmp in find_link.finditer(data):
				data_list[1] = self.__url[:url_prefix] + data[tmp.start()+remove[0][0]:tmp.end()+remove[0][1]]
			for tmp in find_title.finditer(data):
				data_list[2] = data[tmp.start()+remove[1][0]:tmp.end()+remove[1][1]]
			if data_list[2] == "" or data_list[3] == "":
				continue
			data_list[3] = ""
			self.__dataframe.loc[len(self.__dataframe)] = data_list

		print("[+] Dataframe completed")


	def get_dataframe(self):
		return self.__dataframe