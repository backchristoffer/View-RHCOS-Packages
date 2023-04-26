# All of this is purely for testing - It's a work in progress 
import urllib3, requests, re, os
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from requests_html import HTMLSession
from dotenv import load_dotenv

app = Flask(__name__)

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

def createDataFile(input=str, name=str):
    with open(r'{}', 'w').format(name) as fp:
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

def generateDict(input=str):
    clist = input
    pname = []
    for i,k,v in zip(clist[::3],clist[1::3],clist[2::3]):
        pname.extend([[i,k,v]])
    dic = {i[0]: i[1:3] for i in pname}
    return dic

@app.route('/')
def get_data():
    return jsonify(generateDict(readData("data.txt")))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)