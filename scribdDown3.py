import requests
from bs4 import BeautifulSoup
import os
#from pywinauto.application    import Application
#from pywinauto.findwindows    import find_window
#from pywinauto.win32functions import SetForegroundWindow
import webbrowser
#import time
#import pyautogui
#from selenium import webdriver

#InputURL = "https://www.scribd.com/document/261696980/Sec-1-Competition-Math-Training-Handbook"

InputURLs = raw_input("Please enter the Scribd item you wish to download (If multiple, please seperate by commas): ")

InputList = InputURLs.split(",")




for InputURL in InputList:
    #making the output folder
    FolderName = InputURL[InputURL.rfind("/")+1:].replace("-"," ")
    print FolderName

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)


    r = requests.get(InputURL)
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    String_soup = str(soup)

    #now we bascially need 2 things, the docuemtn_id and the key_id

    docID_Index = String_soup.find("document_id") + len("document_id")
    document_ID = String_soup[docID_Index + 2 : String_soup.find(",",docID_Index)]
    print ""
    print "document_id is: " + document_ID

    accKey_Index = String_soup.find("access_key") + len("access_key")
    access_key = String_soup[accKey_Index + 3 : String_soup.find(",",accKey_Index)-1]
    print "access_key is: " + access_key

    template_URL = "http://d1.scribdassets.com/ScribdViewer.swf?document_id=DOCID&access_key=ACCKEY"

    template_URL = template_URL.replace("DOCID", document_ID).replace("ACCKEY", access_key)

    print template_URL

    webbrowser.open(template_URL)
    #time.sleep(15)  #its too hard to do this porperly, selenium doesnt open this site properly)

    #pyautogui.click(950,505)
    #pyautogui.click(125,55)

    #browser = webdriver.Firefox(executable_path='geckodriver.exe')
    #browser.get(template_URL)

    #webbrowser.open(template_URL)

    print "im finished loading"

        #NOTE
        #for some ones, that are completely viewable in the first place, they have a weird structure that while might not break the program, will not be picked up by the program
        #basically, it lists the source JPG file directly in the HTML instead of some weird hoops
        # it should be easy as this is the only place with "orig=" in the html so it should just be fine to download these directly first
        # but thius is to do

