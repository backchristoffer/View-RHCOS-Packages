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

# Render HTML as because of the js script on the rhcos release page
session = HTMLSession()
r = session.get(URL3, verify=False)
r.html.render()
renderedhtml = r.html.html

# Setting up bs4 to use the rendered html above
soup = BeautifulSoup(renderedhtml, 'lxml')

# It is one big table with many rows - Need to sort these 
package_list = []
regex_list = []
buildinfo = soup.find("div", id="buildinfo")
tables = buildinfo.find_all(['th', 'tr'])
for row in tables:
    cells = row.findChildren('td')
    for cell in cells:
        value = cell.string
        package_list.append(value)
        #print(value)

# I need to write this to a file to handle it locally as well for testing purposes. 
"""
with open(r'data.txt', 'w') as fp:
    for item in package_list:
        fp.write("%s\n" % item)
    print('file created')
"""
# TO-DO: Move everything to functions asap, it's way too messy at the moment
# Working with the list down below. Need to use the local file data.txt and sort them in an array
"""
lst = list(range(len(package_list)))
range_list = lst[0::3]
for i in range_list:
    for d in package_list:
        nval = re.search("^{i}-\d+",d)
        regex_list.append(nval)
"""
