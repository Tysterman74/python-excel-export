import easygui
import NewEggService
from flask import Flask
from searchWindows import searchWindows

app = Flask(__name__)

@app.route('/')

def index():
    testResponse = NewEggService.GetResults()
    # testResponse = requests.get(baseurl).content
    print(testResponse)
    return testResponse

# searchwindow=searchWindows()
# searchwindow.runAllWindows()

if __name__ == '__main__':
    app.run(debug=True)
print('starting');
