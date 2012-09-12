import Tkinter
import easygui as eg

from settings import DEBUG

msgbox = eg.msgbox

def getCredentials():
    '''Query user for username and password. Return as a dict

    Future: Add secure password caching
    '''

    msg = "Enter login information"
    title = "Brave IRC Network"
    fieldNames = ['Username', 'Password']
    fieldValues = []  # we start with blanks for the values
    fieldValues = eg.multpasswordbox(msg, title, fieldNames)

    # make sure that none of the fields was left blank
    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "": 
            break # no problems found
        else:
            # show the box again, with the errmsg as the message
            fieldValues = eg.multpasswordbox(errmsg, title, fieldNames, fieldValues)

    if DEBUG:
        fieldValues = 'jnaranjo', 'test'

    credentials = {'username': fieldValues[0], 'password': fieldValues[1]}

    return credentials
