import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

res = requests.get("https://www.geeksforgeeks.org/python/python-programming-language-tutorial/")
# parse the raw HTML content in a cleaner format
soup = BeautifulSoup(res.content, "html.parser")
# Direct the browswer to Google and enter a query
driver = webdriver.Chrome()
driver.get("https://www.toyota.com/")
time.sleep(10)

# print(soup.prettify())
# # print(res.content)
# print(res.status_code)

# # Find the main content container
# # EXtracting content by tag "div" and class_"article--viewer_content"
# content = soup.find("div", class_="article--viewer_content")
# if content:
#     for paragraph in content.find_all('p'):
#         print(paragraph.text.strip())
# else:
#     print("No article content found")

# Some websites load their content dynamically using JavaScript. Meaning the data you
# want to scrape may not be present in the initial HTML source. So BeautifulSoup alone
# won't work

