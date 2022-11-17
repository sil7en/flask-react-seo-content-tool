# import libraries
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def positionsWebscraper(arr):
    arr_return = []

    # Selenium driver for scraping START
    # Selenium custom webddriver (undetected_chromedriver) adjustments
    uc_browser_options = webdriver.ChromeOptions()
    uc_browser_options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    uc_browser_options.add_argument('--lang=es-CL')

    # Create var driver for use uc with chrome options created on last step
    driver = uc.Chrome(options=uc_browser_options)

    # Main iteration to get dicts and links
    # The [:number] define how many sites are going to be scraped
    for obj in arr[:5]:
        url_temp = obj["link"]

        # Selenium driver go to URL
        driver.get(url_temp)
        time.sleep(1.25)
        # Selenium scroll down on the page simulating keyboard action
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.25)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

        # arr to exclude empty strings
        arr_exclude_empty = ['', ' ', '.', '-']

        # prepare driver find elements
        try:
            paragraph = [element.text for element in driver.find_elements(By.TAG_NAME, 'p') if element.text not in arr_exclude_empty]
        except:
            paragraph = []
        try:
            span = [element.text for element in driver.find_elements(By.TAG_NAME, 'span') if element.text not in arr_exclude_empty]
        except:
            span = []
        try:
            h1 = [element.text for element in driver.find_elements(By.TAG_NAME, 'h1') if element.text not in arr_exclude_empty]
        except:
            h1 = []
        try:
            h2 = [element.text for element in driver.find_elements(By.TAG_NAME, 'h2') if element.text not in arr_exclude_empty]
        except:
            h2 = []
        try:
            h3 = [element.text for element in driver.find_elements(By.TAG_NAME, 'h3') if element.text not in arr_exclude_empty]
        except:
            h3 = []
        try:
            h4 = [element.text for element in driver.find_elements(By.TAG_NAME, 'h4') if element.text not in arr_exclude_empty]
        except:
            h4 = []
        try:
            button = [element.text for element in driver.find_elements(By.TAG_NAME, 'button') if element.text not in arr_exclude_empty]
        except:
            button = []
        try:
            li = [element.text for element in driver.find_elements(By.TAG_NAME, 'li') if element.text not in arr_exclude_empty]
        except:
            li = []
        try:
            th = [element.text for element in driver.find_elements(By.TAG_NAME, 'th') if element.text not in arr_exclude_empty]
        except:
            th = []
        try:
            td = [element.text for element in driver.find_elements(By.TAG_NAME, 'td') if element.text not in arr_exclude_empty]
        except:
            td = []
        try:
            a = [element.text for element in driver.find_elements(By.TAG_NAME, 'a') if element.text not in arr_exclude_empty]
        except:
            a = []

        # Get all visible text with Selenium driver and store it in textData
        textData = {
            "TextData": {
                "paragraph" : paragraph,
                "span" : span,
                "h1" : h1,
                "h2" : h2,
                "h3" : h3,
                "h4" : h4,
                "button" : button,
                "li" : li,
                "th" : th,
                "td" : td,
                "a" : a
            }
        }

        # Add textData to obj. Then add it to arr_return
        obj.update(textData)
        arr_return.append(obj)
    
    driver.close()
    return arr_return