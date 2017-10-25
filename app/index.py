import easygui
import NewEggService
import ExportModule
from flask import Flask
from searchWindows import searchWindows

app = Flask(__name__)

@app.route('/')

def index():
    NewEggService.TestUrl()
    # ExportModule.TestCreate()
    # response = NewEggService.GetResults()
    # for excelObj in response:
    #     print(excelObj.name)
    #     print(excelObj.price)
    #     print(excelObj.url)
    #     print(excelObj.vendor)
    # ExportModule.create_excel_sheet_from_data(response, 'dicks_in_my_mouth')
    return 'asdf'

# searchwindow=searchWindows()
# searchwindow.runAllWindows()

if __name__ == '__main__':
    app.run(debug=True)
print('starting')

# def index():
    # tls = TonerLandService()
    # #test = tls.createUrlArray()
    # #results=tls.GetResults()
    # # print(test)
    # results = tls.findContainers()
    # #results=tls.openLocal()
    # print(results)
    # return 'orange'