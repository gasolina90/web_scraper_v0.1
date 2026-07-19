import requests

result = requests.get("https://www.geeksforgeeks.org/python/python-programming-language-tutorial/")
print(result.status_code)
print(result.content)