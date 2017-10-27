import requests
import ExcelObject
import json
import re
import time
from bs4 import BeautifulSoup


class TonerLandService:
    def __init__(self):
        print('Initializing')

# baseURl + Series hardcoded array webscrape or something
# for each series scrape source

 

    def createUrlArray(self):
        baseUrl = 'http://www.tonerland.com/brother/'
        seriesArray = ['dcp-series.html', 'fax-series.html', 'hl-series.html', 'intellifax-series.html', 'mfc-series.html'] 
        PartialURLArray=[]
        for s in seriesArray:
            PartialURLArray.append(baseUrl+s) 
        return PartialURLArray

    def sleep5():
        time.sleep(15)

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

    def FindKeywordIndex(self,array):
        for item in range(1,len(array)):
            if (self.find2ndKeyword(array[item]) and self.find1stKeyword(array[item-1])):
                return item
        return -1

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
        data = self.requestURLs()
        #with open("base.html") as fp:
        sanitized = BeautifulSoup(data.text, 'html.parser')
        # sanitized = BeautifulSoup(fp, 'html.parser')
        sanitized.encode(data.encoding)
        itemContainers=(sanitized.find_all('script', type = "text/javascript"))
        containerLen=len(itemContainers)
        urlList=[]
        for item in range(0,containerLen):
            tempContainer=itemContainers[item].text
            splitContainer=tempContainer.split() 
            keywordIndex=self.FindKeywordIndex(splitContainer)
            if (keywordIndex!=-1):
                urlList=self.findURLS(splitContainer,keywordIndex)

        return urlList

    def requestURLs(self):
        baseURL='http://www.tonerland.com/brother.html'
        headers={
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        } 
        response=requests.get(baseURL, headers=headers, timeout=1)
        return response


    def GoThroughUrls(self, urlList):
        
        urlListLength=len(urlList)
        for url in range(0,urlListLength):
            print(urlList[url])
        # loop through urlList
        # requestURLS
        # parse sk compatible display
        # sleep15()
        # save url list on disc
        # find containers page 2 SearchPrinterModels = findcontainers
        # 
        return 0
        