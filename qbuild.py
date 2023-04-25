# All of this is purely for testing - It's a work in progress 
import urllib3, requests, re, os
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from dotenv import load_dotenv

# Removing the requests insecure warning for now.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Need to use .env for this
load_dotenv()
URL3 = os.getenv('URL3')
getdiffocp = os.getenv('getdiffocp')
getrhcos_streams = os.getenv('getrhcos_streams')

def getPackages(url=str):
    package_list = []
    session = HTMLSession()
    r = session.get(url, verify=False)
    r.html.render()
    renderedhtml = r.html.html
    soup = BeautifulSoup(renderedhtml, 'lxml')
    buildinfo = soup.find("div", id="buildinfo")
    tables = buildinfo.find_all(['th', 'tr'])
    for row in tables:
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.string
            package_list.append(value)
    return package_list

def createDataFile(input=str):
    with open(r'data.txt', 'w') as fp:
        for item in input:
            fp.write("%s\n" % item)
        print('data.txt created')

def readData(input=str):
    package_list = []
    with open(input) as file:
        for i in file:
            i = i.strip()
            package_list.append(i)
    return package_list
        
# TO-DO: Sort list by packages in array
for i in readData("data.txt"):
    print(i)
