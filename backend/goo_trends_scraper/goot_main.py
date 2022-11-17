# import libraries
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# import own functions
#from goo_trends_scraper.goot_queries import gootQueries
from goo_trends_scraper.goot_data import gootData

def gootMain(keyword, gooGeo="CL"):
    # Google Scrapper with Selenium
    # Create var for url
    goot_url_base = 'https://trends.google.com/trends/?geo='
    goot_url = f"{goot_url_base}{gooGeo}"

    # Selenium custom webddriver (undetected_chromedriver) adjustments
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    browser_options.add_argument('--disable-blink-features=AutomationControlled')
    browser_options.add_argument(f'--lang=es-{gooGeo}')

    # Create var driver for use uc with chrome options created on last step
    driver = uc.Chrome(options=browser_options)

    # Selenium go to URL
    driver.get(goot_url)
    driver.maximize_window()
    time.sleep(1.5)

    # Selenium find the searchbox of Google Trends, with 
    goot_search = driver.find_element(By.XPATH, '//div[@class="home-page-header-autocomplete-container"]//following::input')
    goot_search.click()
    time.sleep(1)
    
    # Selenium paste and send keyword to search on Google's search box
    ActionChains(driver)\
        .send_keys(keyword)\
        .send_keys(Keys.DOWN)\
        .send_keys(Keys.ENTER)\
        .perform()
    time.sleep(2)
    
    # Selenium scroll down on the page simulating keyboard action
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.75)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.9)

    # Call own auxiliary functions
    # Call gootTopics to obtain an array with related topics
    goot_type_topics = 'RELATED_TOPICS'
    goot_type_queries = 'RELATED_QUERIES'
    try:
        arr_queries = gootData(driver, goot_type_queries)
        time.sleep(0.66)
    except:
        arr_queries =[]
    
    try:
        arr_topics = gootData(driver, goot_type_topics)
        time.sleep(0.66)
    except:
        arr_topics =[]

    driver.close()

    # Create and fill object/dict to return 
    goot_object = {
        "keyword": keyword,
        "queries": arr_queries,
        "topics": arr_topics
    }

    return goot_object