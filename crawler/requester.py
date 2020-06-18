import requests

from time import sleep
from threading import Thread

class Requester:
    header = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}

    def __init__(self, url_list, num_threads = 4):
        self.__len_urls = len(url_list)
        self.__urls_list = list()

        size = int(len(url_list)/num_threads) + 1
        for i in range(0, len(url_list), size):
            self.__urls_list.append(url_list[i:i+size])
            
        self.__requests = list()
        self.__progress = 0

        self.__set_requests()


    def __set_requests(self):
        # Split the list of URLs to make the requests into multiple threads
        indexer = 0
        threads = list()
        for urls in self.__urls_list:
            thread = Thread(
                    target=self.__set_request_list,
                    args=(urls, indexer)
                    )
            thread.start()
            indexer += 1
            threads.append(thread)

        # Wait for the threads to complete
        for thread in threads:
            thread.join()
            sleep(0.01)
            del thread
        print()

        # Sort the requests in one list only in the same order they were requested
        requests_sorted = sorted(self.__requests, key=lambda x: x[0])
        self.__requests.clear()
        for requests in requests_sorted:
            for request in requests[1]:
                self.__requests.append(request)



    def __set_request_list(self, urls, index):
        requests = (index, list())

        for url in urls:
            request = self.get_one_request(url)
            if request == None:
                continue
            requests[1].append(request)
            self.__progress()
        self.__requests.append(requests)


    def __progress(self):
        self.__progress += 1
        print("[+] {0:05d}/{1:05d} requests completed.".format(
                        self.__progress[0],
                        self.__len_urls), end='\r')


    @staticmethod
    def get_one_request(url):
        timeout = None

        while timeout != False:
            try:
                request = requests.get(url, headers=Requester.header, timeout=5)
                timeout = False
            except (requests.ConnectionError,requests.ReadTimeout):
                timeout = True
                sleep(5)
            except:
                return None

        return request


    def get_requests(self):
        return self.__requests