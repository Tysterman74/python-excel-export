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

    def sleep5():
        time.sleep(15)

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
        return 0
    
    def FindModelUrls(self,itemContainers):
        itemToString = str(itemContainers)
        firstIndex = itemToString.find('href="') + 6
        secondIndex = itemToString.find('"',firstIndex)
        urlItem = itemToString[firstIndex:secondIndex]
        return urlItem

    def FindPrinterModels(self):
        #base2.html goes to http://www.tonerland.com/brother/dcp-series/dcp-110-c.html
        with open("base2.html")as fp:
            sanitized=BeautifulSoup(fp, 'html.parser')
            sanitized.encode(fp.encoding)
            itemContainers=(sanitized.find_all('h2', class_="product-name"))
            containerLen=len(itemContainers)
            for item in range(0,containerLen):
                urlItems=self.FindModelUrls(itemContainers[item])


        return 0
        # loop through urlList
        # requestURLS
        # parse sk compatible display
        # sleep15()
        # save url list on disc
        # find containers page 2 SearchPrinterModels = findcontainers

    def fullParse(self,data):
        title=self.findTitle(data)
        cost=self.findCost(data)
        tableInformation=self.pullTableInformation(data)
        self.pullCompatiblePrinters(data)
        return 0


    def parseFinalPage(self):
        #base3.html goes to http://www.tonerland.com/brother-compatible-ink-black.html
        with open("base3.html") as data:
            finalPage=BeautifulSoup(data,'html.parser')
            finalPage.encode(data.encoding)
            self.fullParse(finalPage)

        return 0

    def findTitle(self,data):
        title = data.find('h1')
        return title.get_text()

    def findCost(self,data):
        cost = data.find(class_='price')
        return cost.get_text()

    def pullTableInformation(self,data):
        tableInformation=[]
        tableRows=data.find_all('td')
        for item in range(0,len(tableRows)-1):# -1 can't pull compatible printers here
            tableInformation.append(tableRows[item].get_text())
        #the Next 4 lines would be what would be given to the Excel exporter
        sku=tableInformation[0] 
        pageYield=tableInformation[1]
        color=tableInformation[2]
        productType=tableInformation[3]

    def pullCompatiblePrinters(self,data):
        CompatiblePrinters = data.find_all(class_="sk_compatible")
        compatiblePrintersList=[]
        for item in CompatiblePrinters:
            compatiblePrintersList.append(item.get_text())
        
        #full list made here! 




        