#import moduel
import requests
from bs4 import BeautifulSoup
import pprint
import os
from queue import Queue

#url queue and parse html
urlq = Queue()
for i in range(5):
    urlq.put('https://www.gooood.cn/page/%s?lang=cn' % str(i))
    while not urlq.empty():
        res = requests.get(str(urlq.get()))
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.entry-title')

     
        #bnb function
        def bnb_gooood(links):
            bnb = []
            for index, item in enumerate(links):
                title = item.getText()
                href = item.get('href', None)
                k = '巴黎'
                if k in title:
                    bnb.append({'title': title, 'link': href})
                    
                    
            return bnb
        final = []
        final.append(bnb_gooood(links))
        


#export the links to a txt file
expt = open('urls.txt','w+')
pprint.pprint(final, stream=expt)
expt.close()
