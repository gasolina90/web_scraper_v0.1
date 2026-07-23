# pip install virtualenv on global python interpreter and check version
# In bottom right corner of VScode: > Select a Python environment > (venv) 
# > Quick Create > Open Terminal > Check for green (.venv) preceeding file path

# pip install beautifulsoup4, and requests

from bs4 import BeautifulSoup
import requests
from xml_parser import etree

url = "https://www.geeksforgeeks.org//"
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, "lxml")
title = soup.title.string

print(f"Title of page: {title}")
