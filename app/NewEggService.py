import requests
import ExcelObject
from bs4 import BeautifulSoup

# class NewEggService:
#     def __init__(self):
#         print('Initializing')

def TestUrl():
    # In order to successful get a hit to a website, we need to mock our User-Agent. This was generated by going to https://www.whoishostingthis.com/tools/user-agent/
    # Future Implementations we should consider importing https://pypi.python.org/pypi/fake-useragent to auto-generate User-Agents so servers won't suspect the same user agent coming into the site.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    # In addition to adding headers, we must also set a timeout as per documentation of the requests module.
    # Not setting a timeout causes the call to continue attempting to call. And can cause a bad, bad time.
    response = requests.get('http://www.tonerland.com/brother/dcp-series.html', headers= headers, timeout=1)
    print(response.text)

def GetResults():
    baseurl = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&' + \
    'Description=brother+cartridges&N=-1&isNodeId=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    response = requests.get('http://www.tonerland.com/brother/dcp-series.html', headers= headers, timeout=1)
    return SanitizeHTML(response)

def SanitizeHTML(html):
    sanitized = BeautifulSoup(html.text, 'html.parser')
    sanitized.encode(html.encoding)
    itemContainers = sanitized.find_all('div', class_='item-container')
    return SanitizeContainers(itemContainers)

def SanitizeContainers(containers):
    listOfProducts = []
    for container in containers:
        price = RetrievePrice(container)
        name = RetrieveName(container)
        url = RetrieveURL(container)
        excelObj = ExcelObject.ExcelObject(name, price, url, 'NewEgg')
        listOfProducts.append(excelObj)
    return listOfProducts

def RetrieveURL(container):
    itemNameContainer = container.find('a', class_='item-title')
    itemElementStr = str(itemNameContainer)
    firstIndex = itemElementStr.find('href="') + 6
    secondIndex = itemElementStr.find('"', firstIndex)
    url = itemElementStr[firstIndex:secondIndex]
    return url

def RetrieveName(container):
    itemNameContainer = container.find('a', class_='item-title')
    return itemNameContainer.get_text()

def RetrievePrice(container):
    itemPriceContainer = container.find('li', class_='price-current')
    dollar = itemPriceContainer.find('strong')
    cent = itemPriceContainer.find('sup')
    return float(dollar.get_text() + cent.get_text())

def SanitizeLinks(links):
    for link in links:
        strLink = str(link)
        print(link)
        firstIndex = strLink.find('href="') + 6
        print('First Index ' + str(firstIndex))
        secondIndex = strLink.find('"', firstIndex)
        print('Second Index ' + str(secondIndex))
        url = strLink[firstIndex:secondIndex]
        print(url)