# import libraries
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# import own functions
from goo_search_scraper.goo_queries import gooQueries
from goo_search_scraper.goo_questions import gooQuestions
from goo_search_scraper.goo_top_positions import gooTopPositions

def gooMain(keyword, googleUrl):
    # Google Scrapper with Selenium
    # Create var for url
    goo_url = googleUrl 

    # Selenium custom webddriver (undetected_chromedriver) adjustments
    uc_browser_options = webdriver.ChromeOptions()
    uc_browser_options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    uc_browser_options.add_argument('--lang=es-CL')

    # Create var driver for use uc with chrome options created on last step
    driver = uc.Chrome(options=uc_browser_options)

    # Selenium go to URL
    driver.get(goo_url)

    # Selenium find the searchbox of Google, called 'q'
    google_search = driver.find_element(By.NAME, 'q')
    # Selenium paste and send keyword to search on Google's search box
    google_search.send_keys(keyword)
    time.sleep(0.33)
    google_search.submit()
    time.sleep(0.5)

    # Call own auxiliary functions
    # Call gooQueries to obtain an array with related queries
    arr_queries = gooQueries(driver)
    arr_top_positions = gooTopPositions(driver)

    # Add custom options to driver to get all Google Related Questions from mobile
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    browser_options.add_argument('--lang=es-CL')
    browser_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    browser_options.add_experimental_option("mobileEmulation", {'deviceName': 'iPhone X'})
    browser_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    new_driver = webdriver.Chrome(options=browser_options)
    new_driver.get(goo_url)
    google_search = new_driver.find_element(By.NAME, 'q')
    google_search.send_keys(keyword)
    time.sleep(0.33)
    google_search.submit()
    time.sleep(0.75)
    google_search = new_driver.find_element(By.NAME, 'q')
    arr_questions = gooQuestions(new_driver)

    # Create and fill object/dict to return 
    goo_object = {
        "keyword": keyword,
        "queries": arr_queries,
        "questions": arr_questions,
        "top_positions": arr_top_positions
    }

    return goo_object