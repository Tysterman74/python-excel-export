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
    keyword="var models"

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

    def parseItemContainer(self, container):
        santizing=container.split()
        return santizing

    def findKeyword(self,word):
        if word==self.keyword:
            return True
        else:
            return False

    def containsKeyWord(self,array):
        for item in array:
            if self.findKeyword(item):
                print(item)
            
                
                


    def findContainers(self):
        with open("base.html") as fp:
            sanitized = BeautifulSoup(fp, 'html.parser')
            #sanitized.encode(fp.encoding)
            itemContainers=(sanitized.find_all('script', type = "text/javascript"))
            itemLen=len(itemContainers)
            for item in itemContainers:
                temp=item.text
                newtemp=temp.split()
                if (len(newtemp)>0):
                    print(len(newtemp))
                    print(newtemp)

                # self.containsKeyWord(newtemp)
            print("not "+self.keyword)
            return itemLen

    


