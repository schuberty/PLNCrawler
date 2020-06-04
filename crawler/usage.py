from pathlib import Path
from os import sep
from sys import argv,exit
from crawler.sites import *

_dir_path = str(Path().absolute()) + sep + "JSONs" + sep

def options():
	if(len(argv) == 1):
		usage()
	elif(len(argv) > 2):
		usage(use=False)
	else:
		if(argv[1].find("start") != -1):
			crawling()
		elif(argv[1].find("select") != -1):
			crawling(getSelection())
		elif(argv[1].find("help") != -1):
			usage()
		else:
			usage(use=False)


def crawling(selection=[True, True, True, True]):
	if(not Path(_dir_path).is_dir()):
		print("[!] The directory 'JSONs' is missing and it'll be created.")
		Path(_dir_path).mkdir(exist_ok=True)
	print("[+] All your crawled data will be stored in:\n\t'{0}'".format(_dir_path))

	if(selection[0]):
		sensacionalista = get_sensacionalista_data()
		sensacionalista.to_json(_dir_path+"sensacionalista.json", orient="records",
														lines=True, force_ascii=False)
	if(selection[1]):
		piaui_herald = get_piauiherald_data()
		piaui_herald.to_json(_dir_path+"piau_herald.json", orient="records",
														lines=True, force_ascii=False)
	if(selection[2]):
		huffpost = get_huffpostbrasil_data()
		huffpost.to_json(_dir_path+"huffpost.json", orient="records", lines=True, force_ascii=False)
	if(selection[3]):
		nexojornal = get_nexojornal_data()
		nexojornal.to_json(_dir_path+"nexojornal.json", orient="records",
														lines=True, force_ascii=False)


def getSelection():
	print('-'*40+"""
\tSensacionalista...: 1
\tThe piaui Herald..: 2 
\tHuffPost Brasil...: 3
\tNexo Jornal.......: 4
\tCancel/Exit.......: 5\n""")
	num = int(input("\tChoose one number\n>>> "))
	if(0 < num < 5):
		selections = [False, False, False, False]
		selections[num-1] = True
		return selections
	elif(num == 5):
		print("Canceled and exiting.")
	else:
		print("Invalid number. Exiting.")
	exit()


def usage(use=True):
	use = ("Correct use", "Usage")[use]
	print('-'*40+'\n'+"""{0}:\t$ python {1} <option>
\tOptions:
\t\tstart  : Crawl all 4 websites
\t\tselect : Choose one to crawl
\t\thelp   : Show this""".format(use,argv[0]))