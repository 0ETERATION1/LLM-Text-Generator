import requests
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_all_text_with_javascript(url):
    # Setup Selenium with ChromeDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # Comment if you want the browser window to open
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to the website
    driver.get(url)

    body_text = driver.find_element(By.TAG_NAME, "body").text

    ##print(body_text)

    driver.quit()
    
    return body_text


def get_text_by_tag(url, tag_name="body", class_name=None):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    
    elements_text = []
    try:
        if class_name:
            elements = driver.find_elements(By.CLASS_NAME, class_name)
        else:
            elements = driver.find_elements(By.TAG_NAME, tag_name)
        
        for element in elements:
            elements_text.append(element.text)
    finally:
        driver.quit()
    
    return "\n".join(elements_text)


# Replace with the URL you want to scrape
#url = 'https://www.cs.umd.edu/'

# calling the function
#get_all_text_with_javascript(url)