from json import load as load_json
from pathlib import Path
from os import sep

from crawler.algorithms import Crawler

dir_path = str(Path().absolute()) + sep

class Sites():
    def __init__(self):
        self.__sites = []
        for site in self.get_json_file():
            self.__sites.append(Site(site[0],site[1]))


    def get_json_file(self):
        with open(dir_path + "sites.json", 'r') as file:
            json_file = load_json(file)
            
        sites = []
        for site in json_file.items():
            sites.append([site[0],site[1]])

        return sites

    
    def print_sites(self):
        for item in self.__sites:
            print(item.get_name(), end='\n' + '-'*40 + '\n')
            for arg in item.get_args():
                print(arg)
            print()


class Site():
    def __init__(self, name, args):
        self.__name = name
        self.__args = args

        self.__crawler = Crawler(**self.__args[0])

        self.process()

        self.__crawler.get_dataframe().to_json(
            dir_path + self.__name + ".json",
            orient = "records",
            lines = True,
            force_ascii = False
        )
    
    def process(self):
        self.__crawler.set_pages(**self.__args[1])
        self.__crawler.set_raw_data(**self.__args[2])
        self.__crawler.set_data_frame(**self.__args[3])

    def get_name(self):
        return self.__name
    
    def get_args(self):
        return self.__args