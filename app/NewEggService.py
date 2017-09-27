import requests
from bs4 import BeautifulSoup

# class NewEggService:
#     def __init__(self):
#         print('Initializing')

def GetResults():
    baseurl = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&' + \
    'Description=brother+cartridges&N=-1&isNodeId=1'
    response = requests.get(baseurl)
    print(response.headers)
    print(response.encoding)
    # print(response.content)
    SanitizeHTML(response)
    # print(response.text)
    return 'asdf'

def SanitizeHTML(html):
    sanitized = BeautifulSoup(html.text, 'html.parser')
    sanitized.encode(html.encoding)
    linkHTML = sanitized.find_all('a', class_='item-title')
    SanitizeLinks(linkHTML)

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
