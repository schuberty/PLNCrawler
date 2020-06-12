from json import load as load_json
from pathlib import Path
from os import sep

dir_path = str(Path().absolute()) + sep

class Site():
    
    def __init__(self):
        with open(dir_path + "sites.json", 'r') as file:
            self.__json_file = load_json(file)