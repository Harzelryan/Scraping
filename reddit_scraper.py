#Import libraries
import urllib.request
from bs4 import BeautifulSoup
import json
import numpy as np
import pandas as pd

url = "https://old.reddit.com/top/"

#get the HTML content
request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()

#Parse the content using beautifulsoup
soup = BeautifulSoup(html, 'html.parser')

main_table = soup.find("div", attrs={"id" : "siteTable"})
links = main_table.find_all("a", class_ = "title")

#from each link extract the text of link and the link itself
#List to store a dict of the data we extracted 

extracted_records = []
for link in links:
    title = link.text
    url = link['href']
    
    if not url.startswith('http'):
        url = "https://reddit.com"+url
        
    records = {"title" : title , "link" : url}
    
    extracted_records.append(records)
    

print(extracted_records)

#Store the content as a json
with open('data.json', 'w') as outfile:
    json.dump(extracted_records, outfile)

#open the json file
with open('data.json', 'r') as infile: # load the data into a Python dictionary
   data = json.load(infile) # print the data print(data)
    
