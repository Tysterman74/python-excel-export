import easygui
import NewEggService
from TonerLandService import TonerLandService
from flask import Flask
from searchWindows import searchWindows



app = Flask(__name__)

@app.route('/')

# def index():
#     testResponse = NewEggService.GetResults()
#     for excelObj in testResponse:
#         print(excelObj.name)
#         print(excelObj.price)
#         print(excelObj.url)
#         print(excelObj.vendor)
#     return 'asdf'
  
def index():
    tls = TonerLandService()
    #test = tls.createUrlArray()
    #results=tls.GetResults()
    # print(test)
    results = tls.findContainers()
    #results=tls.openLocal()
    print(results)
    return 'orange'

# searchwindow=searchWindows()
# searchwindow.runAllWindows()

if __name__ == '__main__':
    app.run(debug=True)
print('starting')

