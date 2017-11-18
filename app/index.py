import easygui
import NewEggService
from TonerLandService import TonerLandService
from ExcelWriter import ExcelWriter
from flask import Flask
from searchWindows import searchWindows

app = Flask(__name__)

@app.route('/')



def index():
    tls = TonerLandService()
    # NewEggService.TestUrl()
    # ExportModule.TestCreate()
    # response = NewEggService.GetResults()
    # for excelObj in response:
    #     print(excelObj.name)
    #     print(excelObj.price)
    #     print(excelObj.url)
    #     print(excelObj.vendor)
    # ExportModule.create_excel_sheet_from_data(response, 'dicks_in_my_mouth')
    #test=tls.findContainers()
    # test2=tls.readListFromFile()
    #tls.writeListToFile(test)
    #test=tls.readListFromFile()
    #tls.FindPrinterModels('http://www.tonerland.com/brother/dcp-series/dcp-110-c.html')
    #tls.parseFinalPage()
    #tls.GoThroughUrls(test)
    #tls.makeMainUrlList()
    # tls.parseFinalPage()
    a=tls.CreateUrlList()
    tls.CreateExcelArray(a)
    
    return 'asdf'

# searchwindow=searchWindows()
# searchwindow.runAllWindows()

if __name__ == '__main__':
    app.run(debug=True)
print('starting')
