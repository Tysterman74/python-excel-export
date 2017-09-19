import easygui;
print('starting');

msg = "Enter your search Query, Then push OK"
title = "Item Finder"
fieldNames = ["Item Query 1","Item Query 2","Item Query 3","Item Query 4","Item Query 5"]
fieldValues = []  # we start with blanks for the values
fieldValues = easygui.multenterbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:
    if fieldValues is None: break
    errmsg = ""
    for i in range(len(fieldNames)):
        if fieldValues[i].strip() == "":
            errmsg += ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "":
        break # no problems found
    fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)

print("Reply was: %s" % str(fieldValues))

result = easygui.enterbox(msg='Enter something.', title='fire', default='', strip=True, image=None, root=None)
print(result)
