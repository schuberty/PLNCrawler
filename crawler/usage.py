from pathlib import Path  #abosulute func
from os import sep
from sys import argv
from crawler.sites import *

def options():
	if(len(argv) == 1):
		usage()
	elif(len(argv) > 2):
		usage(use=False)
	else:
		if(argv[1].find("start") != -1):
			crawler()
		elif(argv[1].find("select") != -1):
			crawler(start=False)
		else:
			usage(use=False)


def crawler(start=True):
	if(start):
		print("TO-DO1")
	else:
		print("TO-DO2")


def usage(use=True):
	use = ("Correct use", "Usage")[use]
	print("-"*40+'\n'+"""{0}:\t$ python {1} <option>
\tOptions:
\t\tstart  : Crawl all 4 websites
\t\tselect : Choose one to crawl
		""".format(use,argv[0]), end='')