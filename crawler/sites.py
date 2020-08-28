import pandas as pd

from json import load as load_json
from pathlib import Path
from os import sep

from crawler.algorithms import Crawler

dir_path = str(Path().absolute()) + sep

class Sites():

    datasets_dir = dir_path + sep + "datasets" + sep 

    def __init__(self):
        self.__sites = list()

        if not Path(self.datasets_dir).is_dir():
            Path(self.datasets_dir).mkdir(exist_ok=True)

        for site in self.get_json_file():
            self.__sites.append(Site(site[0],site[1]))


    def get_json_file(self):
        with open(dir_path + "sites.json", 'r') as file:
            json_file = load_json(file)
            
        sites = []
        for site in json_file.items():
            sites.append([site[0],site[1]])

        return sites


class Site():
    def __init__(self, name, args):
        self.__name = name
        self.__args = args

        self.__crawler = Crawler(**self.__args[0])
        self.process()
        self.__dataframe = pd.DataFrame(self.__crawler.get_data(), columns=["is_sarcastic","article_link","headline","text"])

        # data = self.__crawler.get_data()
        # file = Sites.datasets_dir + "texto_" + self.__name + ".txt"
        # f = open(file, "w+", encoding="utf-8")
        # for d in data:
        #     if(d[3] == None):
        #         continue
        #     f.write(d[3])
        # f.close()

        # self.__dataframe.to_csv(
        #     Sites.datasets_dir + self.__name + ".csv",
        #     sep = '|',
        #     index = False,
        #     encoding = "utf-8-sig"
        # )
        self.__dataframe.to_json(
            Sites.datasets_dir + self.__name + ".json",
            orient = "records",
            lines = True,
            force_ascii = False
        )
    
    def process(self):
        self.__crawler.set_requests(**self.__args[1])
        self.__crawler.set_data(**self.__args[2])

    def get_name(self):
        return self.__name
    
    def get_args(self):
        return self.__args