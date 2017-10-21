import requests
import ExcelObject
import json
from bs4 import BeautifulSoup


class TonerLandService:
    def __init__(self):
        print('Initializing')

# baseURl + Series hardcoded array webscrape or something
# for each series scrape source
# 
# 
#
    
    def createUrlArray(self):
        baseUrl = 'http://www.tonerland.com/brother/'
        seriesArray = ['dcp-series.html', 'fax-series.html', 'hl-series.html', 'intellifax-series.html', 'mfc-series.html'] 
        PartialURLArray=[]
        for s in seriesArray:
            PartialURLArray.append(baseUrl+s) 
        return PartialURLArray
            

    def GetResults(self):
        response = requests.get('file:///base.html',timeout=5)
        return response.text

    def findContainers(self):
        with open("base.html") as fp:
            sanitized = BeautifulSoup(fp)
            #sanitized.encode(fp.encoding)
            itemContainers= json.loads(sanitized.find_all('script', type='text/javascript').text)
            return itemContainers['url']
