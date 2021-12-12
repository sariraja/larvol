from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\larvol\\chromedriver.exe")
driver.get('https://www.abstractsonline.com/pp8/#!/9330')

element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body"]/div/div[2]/div[2]')))
print(element.text)
find_href = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'a')))
for my_href in find_href:
    print(my_href.get_attribute("href"))
link_1=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/ul/li[1]/a')))
ActionChains(driver).key_down(Keys.CONTROL).click(link_1).key_up(Keys.CONTROL).perform()
driver.switch_to.window(driver.window_handles[1])
url = driver.current_url
print(url)

elem= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="results"]')))
all_li = elem.find_elements_by_class_name("bodyTitle")
f2= open('Conf Web Planner.csv','w')
for li in all_li:
    text = li.text
    f2.write("\n")
    f2.write(text)

all_date = elem.find_elements_by_class_name("session-date")
for date in all_date:
    text = date.text
    f2.write("\n")
    f2.write(text)
all_location = elem.find_elements_by_class_name("location")
for location in all_location:
    text = location.text
    f2.write("\n")
    f2.write(text)
f2.close()