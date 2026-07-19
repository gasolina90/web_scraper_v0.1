import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.geeksforgeeks.org/python/python-programming-language-tutorial/")
# parse the raw HTML content in a clean readable format
soup = BeautifulSoup(res.content, "html.parser")

# print(soup.prettify())
# # print(res.content)
# print(res.status_code)

# Find the main content container
content = soup.find("div", class_="article--viewer_content")
if content:
    for paragraph in content.find_all('p'):
        print(paragraph.text.strip())
else:
    print("No article content found")
