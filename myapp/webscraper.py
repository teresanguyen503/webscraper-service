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

driver.close()

