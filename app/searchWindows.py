import easygui;

class searchWindows(object):
    def searchBoxGo(self):
        msg = "Enter a search Query, Then push OK"
        title = "Item Finder"
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.enterbox(msg,title, fieldValues)

        # make sure that none of the fields was left blank
        while 1:
            if fieldValues is None: break
            errmsg = ""
            for i in range(len(fieldValues)):
                if fieldValues[i].strip() == "":
                    errmsg += ('"%s" is a required field.\n\n' % fieldValues[i])
            if errmsg == "":
                break # no problems found
            fieldValues = easygui.enterbox(errmsg, title, fieldValues)

        #print("Reply was: %s" % str(fieldValues))
        return fieldValues;

        
    def msgBoxGo(self,fieldValue):
        msgWindow="Searching for %s" %str(fieldValue)
        easygui.msgbox(msgWindow)
        #message window saying we are searching for the search term

    def resultsBoxGo(self):
        easygui.msgbox("Here are the results")

    def ynBoxGo(self):
        ynboxQuestion="Would you like to export as an Excel ?"
        ynboxTitle="ExportExcel"
        ynResult=easygui.ynbox(ynboxQuestion,ynboxTitle)
        #print(ynResult)

    def runAllWindows(self):
        searchBoxResult = self.searchBoxGo()
        self.msgBoxGo(searchBoxResult)
        self.resultsBoxGo()
        self.ynBoxGo()
