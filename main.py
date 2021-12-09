from bs4 import BeautifulSoup
import requests
from selenium import webdriver

url ="https://www.abstractsonline.com/pp8/#!/9330/"
headers = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(url, headers=headers)

print(r.status_code)


browser = webdriver.Firefox()
browser.get(url)
soup = BeautifulSoup(r.text, "html.parser")
print(soup)
