import bs4
from bs4 import BeautifulSoup
import requests
import re 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.common.by import By


service = Service(ChromeDriverManager().install())

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=service, 
    options=options
)

url = "https://www.vitaminshoppe.com/search/categories/pre-workout?search=pre%20workout"
driver.get(url)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

page_text = soup.find(class_="victory-pagination").ul.find_all('li')
pages = int(str(page_text).split("/")[-3].split(">")[-1][:-1])
print(pages)

driver.close()

