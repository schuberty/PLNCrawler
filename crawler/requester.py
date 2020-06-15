import requests

from time import sleep
from queue import Queue
from threading import Thread

class Requester:
    __header = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}

    def __init__(self, url_list, __list_size=25):
        self.__url_list = url_list
        self.__list_size = 25
        
        self.__threads = list()
        self.__requests = list()

        self.set_requests()


    def set_requests(self):
        progress = 0
        indexer = 0
        for i in range(0, len(self.__url_list), self.__list_size):
            thread = Thread(
                    target=self.get_urls_requests,
                    args=(self.__url_list[i:i+self.__list_size], indexer)
                    )
            thread.start()
            indexer += 1
            self.__threads.append(thread)

        print("{0:03d}/{1:03d} threads completed".format(progress,len(self.__threads)), end='\r')
        for thread in self.__threads:
            thread.join()
            progress += 1
            print("{0:03d}/{1:03d} threads completed".format(progress,len(self.__threads)), end='\r')
            sleep(0.01)
        print()

        requests_sorted = sorted(self.__requests, key = lambda x: x[0])
        self.__requests.clear()

        for requests in requests_sorted:
            for request in requests[1]:
                self.__requests.append(request)
            

    def get_urls_requests(self, urls, index):
        requests = (index, list())
        for url in urls:
            request = self.get_one_request(url)
            if request == None:
                continue
            requests[1].append(request)
        self.__requests.append(requests)
    
    
    def get_one_request(self, url):
        timeout = True

        while timeout == True:
            try:
                request = requests.get(url, headers=self.__header, timeout=5)
                timeout = False
            except (requests.ConnectionError,requests.ReadTimeout):
                timeout = True
                sleep(5)
            except:
                return None

        return request


    def get_requests(self):
        return self.__requests 