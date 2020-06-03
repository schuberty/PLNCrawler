from crawler.algorithms import *

_header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}

def get_sensacionalista_data():
  """
  Get Sensacionalista sarcastic articles, related to Brazil, data.
  Link is 'https://www.sensacionalista.com.br/pais'.

  Returns
  -------
  pd.DataFrame
    Dataframe containing all the crawling information
  """
  url = "https://www.sensacionalista.com.br/pais/page/"

  last_page = get_last_page(url, "last", r"title=\"[^\"]*", 7, 0)

  htmls = get_requests(url, last_page)

  raw_data = get_raw_data(htmls, "td_module_8 td_module_wrap", r"<a[^<]*</a>")

  data_frame = get_data_frame(raw_data, True,
                              r"href=\"[^\"]*", r"title=\"[^\"]*",
                              [6,7], [0, 0])

  return data_frame


def get_piauiherald_data():
  """
  Get The piau Herald sarcastic articles data.
  Link is 'https://piaui.folha.uol.com.br/herald/'.

  Returns
  -------
  pd.DataFrame
    Dataframe containing all the crawling information

  Note
  ----
  The piau Herald website don't use a page link list;
    e.g. 'Page 1, 2, 3, ..., 51, 52'
  Instead, it uses an archived section by year of the news. So the URLs of those
  sections and the requests are all made at once
  """
  url = "https://piaui.folha.uol.com.br/herald/"


  htmls = []
  find_years = re.compile(r"data-tab=\"arquivo_\d{4}\">")
  html = requests.get(url, headers=_header)
  bs = BeautifulSoup(html.text, "html.parser")
  li = str(bs.find_all("li", class_="tab-btn"))
  for year in find_years.finditer(li):
    htmls.append(requests.get(str(url[:-7] + li[year.start()+18:year.end()-2]), headers=_header))

  raw_data = get_raw_data(htmls, "bloco size-2", r"<a href=[^>]*>\s<h2[^<]*")

  data_frame = get_data_frame(raw_data, True, 
                              r"<a href=\"[^\"]*\">", r"<h2 class=\"bloco-title\">\s*.*",
                              [9,26], [2,0])

  return data_frame


def get_huffpostbrazil_data():
  """
  Get HuffPost Brazil news data.
  Link is 'https://www.huffpostbrasil.com/noticias/'.

  Returns
  -------
  pd.DataFrame
    Dataframe containing all the crawling information
  """
  url = "https://www.huffpostbrasil.com/noticias/"

  last_page = get_last_page(url, "pagination__link", r"href=\"/noticias/\d*/\"", 16, 2)

  htmls = get_requests(url, last_page)

  raw_data = get_raw_data(htmls, "apage-rail-cards", r"<a class=\"[^<]*</a>")

  data_frame = get_data_frame(raw_data, False,
                              r"href=\"[^\"]*\"", r"target=\"_self\">[^<]*<",
                              [7,15], [1,1], url=url[:-9])
  
  return data_frame


def get_nexojornal_data():
  """
  Get Nexo Jornal news about society data.
  Link is 'https://www.nexojornal.com.br/tema/Sociedade'.

  Returns
  -------
  pd.DataFrame
    Dataframe containing all the crawling information
  """
  url = "https://www.nexojornal.com.br/tema/Sociedade?pagina="

  last_page = get_last_page(url+"1", "Pagination__link___1VkYg", r">\d{3}</a>", 1, 4)

  htmls = get_requests(url, last_page)

  raw_data = get_raw_data(htmls, "Teaser__title-dark___1HEzZ", r"<a alt=\"[^>]*>", element="h4")

  data_frame = get_data_frame(raw_data, False,
                              r"href=\"[^\"]*\"", r"title=\"[^\"]*\">", 
                              [6,7], [1,2], url=url[:-23])

  return data_frame