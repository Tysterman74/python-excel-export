import requests
import re
import time
from ExcelWriter import ExcelWriter
from bs4 import BeautifulSoup


class TonerLandService:
    def __init__(self):
        print('Initializing Toner Land Service')

# baseURl + Series hardcoded array webscrape or something
# for each series scrape source

    def sleep15():
        time.sleep(15)
            
    def FindManufacturer(self):
        test="dcp-series fax-series hl-series intellifax-series mfc-series"
        p=re.compile('(dcprance)')
        if (p.search(test) is None):
            print("Could Not Find a match")
        else: 
            print("I found a Match")
    
    def writeListToFile(self,listData):
        file = open("urlList.txt","w")
        for item in listData:
            file.write(item + '\n')
        file.close()

    def writeUrlToFile(self,urlData):
        file = open("urlList2.txt","a+")
        file.write(urlData + '\n')
        file.close()

    def readListFromFile(self):
        urlTemp=[]
        with open('urlList.txt','r+') as data:
            for line in data:
                urlTemp.append(line[:-1])
            return urlTemp

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

    def requestURLs(self,url):
        headers={
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        } 
        response=requests.get(url, headers=headers, timeout=5)
        return response

    def GoThroughFirstUrls(self, urlList):
        urlListLength=len(urlList)
        for url in range(0,urlListLength):
            print(urlList[url])
            self.FindPrinterModels(urlList[url])         
    
    def FindModelUrls(self,itemContainers):
        itemToString = str(itemContainers)
        firstIndex = itemToString.find('href="') + 6
        secondIndex = itemToString.find('"',firstIndex)
        urlItem = itemToString[firstIndex:secondIndex]
        return urlItem

    def FindPrinterModels(self,url):
        #base2.html goes to http://www.tonerland.com/brother/dcp-series/dcp-110-c.html
        data = self.requestURLs(url)
        sanitized=BeautifulSoup(data.text, 'html.parser')
        sanitized.encode(data.encoding)
        itemContainers=(sanitized.find_all('h2', class_="product-name"))
        containerLen=len(itemContainers)
        for item in range(0,containerLen):
            urlItems=self.FindModelUrls(itemContainers[item])
            # print(urlItems)
            self.writeUrlToFile(urlItems)
        return 0

    def makeMainUrlList(self):
        
        urlList=self.readListFromFile()
        self.GoThroughFirstUrls(urlList)

    def fullParse(self,data):
        title=self.findTitle(data)
        cost=self.findCost(data)
        sku=self.findSKU(data)
        pageYield=self.findPageYield(data)
        color=self.findColor(data)
        productType=self.findProductType(data)

        compatiblePrinters=self.pullCompatiblePrinters(data)
        # print(compatiblePrinters)
        excelArray=[title,cost,sku,pageYield,color,productType,compatiblePrinters]
        return excelArray
        #return excelArray
    
    def parseFinalPage(self,urlName):
        #base3.html goes to http://www.tonerland.com/brother-compatible-ink-black.html
        # with open("base3.html") as data:
        data=self.requestURLs(urlName)
        finalPage=BeautifulSoup(data.text,'html.parser')
        finalPage.encode(data.encoding)
        excelArray=self.fullParse(finalPage)
        excelArray.append(urlName)
        return excelArray

    def findTitle(self,data):
        title = data.find('h1')
        return title.get_text()

    def findCost(self,data):
        cost = data.find(class_='price')
        return cost.get_text()




    def findSKU(self,data):
        table=data.find('th',text='SKU')
        if (table==None):
            return "N/A"
        else:
            sku=table.findNext('td')
            skuText=sku.text
            return skuText

    def findPageYield(self,data):
        table=data.find('th',text='Page Yield')
        if (table==None):
            return "N/A"
        else:
            pageYield=table.findNext('td')
            pyText=pageYield.text
            return pyText

    def findColor(self,data):
        table=data.find('th',text='Color')
        if (table==None):
            return "N/A"
        else:
            color=table.findNext('td')
            cText=color.text
            return cText

    def findProductType(self,data):
        table=data.find('th',text='Type of Product')
        if (table==None):
            return "N/A"
        else:
            productType=table.findNext('td')
            ptText=productType.text
            return ptText
        
        



    def pullCompatiblePrinters(self,data):
        CompatiblePrinters = data.find_all(class_="sk_compatible")
        compatiblePrintersList=[]
        for item in CompatiblePrinters:
            compatiblePrintersList.append(item.get_text())
        strConvert1="".join(compatiblePrintersList)
        strConvert2=strConvert1.replace('\n',',')
        strConvert3=strConvert2[1:-1]
        return strConvert3
        #full list made here! 

    def CreateUrlList(self):
        eList=[]
        with open('urlList2.txt','r+') as data:
            for line in data:
                eList.append(line[:-1])
            return eList
    
    def CreateExcelArray(self,urlList):
        e=ExcelWriter()
        urlListLen=len(urlList)    
        for i in range(1986,urlListLen):
            indexString=self.makeIndexAndUrl(i,urlList[i])
            print(indexString)
            excelArray=self.parseFinalPage(urlList[i])
            print('excelArray made')
            e.appendToExcelSheet(excelArray)
            print("added to Excel")
            

    def makeIndexAndUrl(self,index,url):
        indexStr=''
        indexStr+=str(index)
        indexStr+=' '
        indexStr+=url
        return indexStr
            
    
        
        
        




        