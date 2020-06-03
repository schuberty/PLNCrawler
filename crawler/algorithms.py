import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

_header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}

def get_last_page(
    url: str,
    html_class: str,
    re_string: str,
    rm_start: int,
    rm_end: int
  ) -> int:
  """
  Get the last page number of a specific website.

  Parameters
  ----------
  url : str
    Website URL to find the last page it has
  html_class : str
    Class of the a href attribute related to the maximum number
  re_string : raw str
    Regular expression to find the last page refer
  rm_start : int
    How much to exclude from the beginning of the substring founded by the RE
  rm_end : int
    How much to exclude from the end of the substring founded by the RE

  Returns
  -------
  int
    Last page number founded of a specific website
  """
  find_last_page = re.compile(re_string)

  url = url + '1'
  html = requests.get(url, headers=_header)
  bs = BeautifulSoup(html.text, "html.parser")
  element = str(bs.find_all("a", class_=html_class))
  for page in find_last_page.finditer(element):
    last_page = int(element[page.start()+rm_start:page.end()-rm_end])

  return last_page


def get_requests(
    url: str,
    last_page: int
  ) -> list:
  """
  Get all requests from a URL, from the first to the last page.

  Parameters
  ----------
  url : str
    Website URL to get all requests
  last_page : int
    The website URL last page

  Returns
  -------
  list
    All page requests from first to last page

  Note
  ----
  May occurs an error if any type of internet interference happens.
  """
  htmls = []
  
  for page_num in range(1, last_page):
    page_url = url + str(page_num)
    html = requests.get(page_url, headers=_header)
    htmls.append(html)
  
  return htmls


def get_raw_data(
      htmls: list,
      html_class: str,
      re_element: str,
      element: str="div"
    ) -> list:
  """
  Get a specified part of a HTML page text from a element and class

  Parameters
  ----------
  htmls : list
    A HTML request list
  html_class : str
    Class of the a specified element
  re_element : str
    Regular expression to find a specific HTML element
  element : str, default "div"
    Element of the HTML to be founded

  Returns
  -------
  list
    All the htmls data splited by a specific element class and RE
  """
  find_anchor = re.compile(re_element)
  raw_data = []

  for html in htmls:
    bs = BeautifulSoup(html.text, "html.parser")
    raw = str(bs.find_all(element, class_=html_class))
    for anc in find_anchor.finditer(raw):
      raw_data.append(raw[anc.start():anc.end()])
  
  return raw_data


def get_data_frame(
      raw_data: str,
      sarcasm: bool,
      re_link: str,
      re_title: str,
      rm_start: tuple,
      rm_end: tuple,
      url: str=""
    ) -> pd.DataFrame:
  """
  Get a specific data of links and title information from a list of HTML
  specific data

  Parameters
  ----------
  raw_data : str
    A HTML data list splited by a specific element class and RE
  sarcasm : bool
    If the article containing is sarcastic or not
  re_link : str
    Regular expression to find a href HTML element
  re_title : str
    Regular expression to find a title HTML element
  rm_start : tuple, (int,int)
    How much to exclude from the beginning of two substrings founded by the
    two regular expressions: re_link and re_title, in that order
  rm_end : tuple, (int,int)
    How much to exclude from the end of two substrings founded by the two
    regular expressions: re_link and re_title, in that order
  url : str, default ""
    A substring to add in the beginning of the link founded by the re_link;
    It's only used if the website URL is different from the original used in
    the crawling

  Returns
  -------
  pd.DataFrame
    Dataframe containing all the informatiom
  """
  find_link = re.compile(re_link)
  find_title = re.compile(re_title)

  data_frame = pd.DataFrame(columns=["article_link","headline","is_sarcastic"])

  for data in raw_data:
    data_list = [[],[],[]]
    for tmp in find_link.finditer(data):
      data_list[0] = url + data[tmp.start()+rm_start[0]:tmp.end()+rm_end[0]]
    for tmp in find_title.finditer(data):
      data_list[1] = data[tmp.start()+rm_start[1]:tmp.end()+rm_end[1]]
    if(data_list[1] == ""): continue
    data_list[2] = sarcasm
    data_frame.loc[len(data_frame)] = data_list
  
  return data_frame