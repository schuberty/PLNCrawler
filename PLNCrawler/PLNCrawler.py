from sys import version_info

from crawler.sites import Sites

if version_info[0] < 3:
	raise Exception("PLNCrawler requires at least python3.8")
if version_info[0] < 3 and version_info[1] < 8:
	raise Exception("PLNCrawler requires at least python3.8")

def _main():
	Sites()

if __name__ == '__main__':
	_main()