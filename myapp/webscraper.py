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

object_list = {}

for page in range(1, pages + 1):
    service = Service(ChromeDriverManager().install())

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=service, 
        options=options
    )

    url = f"https://www.vitaminshoppe.com/search/categories/pre-workout?search=pre%20workout&page={page}"
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser") 

    
    all_links = soup.find_all(class_="gridClass")
    print(len(all_links))
    for product in all_links: 
        brand = product.find(class_="product-info product-grid").text
        brand_detail = product.find(class_="product-info product-name").text
        price = product.find(class_="sale-price product-sale-price").text
        a_link = product.find(class_="plp--tile--product-Image-wrapper").find('a', href=True)['href']

        if brand in object_list: 
            while brand in object_list: 
                brand += "*"
            object_list[brand] = {
                "brand details": brand_detail, 
                "price": price, 
                "website": "https://www.vitaminshoppe.com" + a_link 
            }
        else: 
            object_list[brand] = {
                "brand details": brand_detail, 
                "price": price, 
                "website": "https://www.vitaminshoppe.com" + a_link 
            }

driver.close()

