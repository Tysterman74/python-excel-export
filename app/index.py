import easygui
import window
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    baseurl = 'http://m.newegg.com/ProductList?description=LCD+TV&categoryId=411' + \
          '&storeId=10&nodeId=7719&parentCategoryId=264&isSubCategory=true&' + \
          'categoryType=1'
    testResponse = requests.get(baseurl).content
    print(testResponse)
    return testResponse;

if __name__ == '__main__':
    app.run(debug=True)