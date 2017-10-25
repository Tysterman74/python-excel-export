import requests
import ExcelObject
import json
import re
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

    def parseItemContainer(self, container):
        santizing=container.split()
        return santizing

    def find1stKeyword(self,word):
        firstWord='var'
        
        if word==firstWord:
            return True
        else:
            return False
    

    def find2ndKeyword(self,word):
        secondWord='models'

        if word==secondWord:
            return True
        else:
            return False

    def findURLKeyword(self,word):
        urlKeyword='url:'
        if word==urlKeyword:
            return True
        else: 
            return False

    def SearchKeyWord(self,array):
        
        for item in range(1,len(array)):
            if (self.find2ndKeyword(array[item]) and self.find1stKeyword(array[item-1])):
                return(self.findURLS(array,item))

    def findURLS(self,array,index):
        listOfURLs=[]
        for item in range(index,len(array)):
            if(self.findURLKeyword(array[item])):
                listOfURLs.append(array[item+1][1:-4])
        return(listOfURLs)
            
    def FindManufacturer(self):
        test="dcp-series fax-series hl-series intellifax-series mfc-series"
        p=re.compile('(dcprance)')
        if (p.search(test) is None):
            print("Could Not Find a match")
        else: 
            print("I found a Match")

    def findContainers(self): #works for first page to find the urls
        with open("base.html") as fp:
            sanitized = BeautifulSoup(fp, 'html.parser')
            #sanitized.encode(fp.encoding)
            itemContainers=(sanitized.find_all('script', type = "text/javascript"))
            temp=itemContainers[29].text
            newtemp=temp.split()
            listtemp=self.SearchKeyWord(newtemp)
            print(listtemp)
            #self.FindManufacturer()
            return 0




