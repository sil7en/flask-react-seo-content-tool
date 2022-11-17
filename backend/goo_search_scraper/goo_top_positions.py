from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to obtain top organic positions of a query, using Selenium webdriver
def gooTopPositions(wd):
    wd.maximize_window()
    arr_return = []
    time.sleep(0.5)
    google_top_positions = wd.find_elements(By.CLASS_NAME, 'MjjYud')

    # position_counter created to store actual position number of a Google's result
    postion_counter = 1
    for position in google_top_positions:
        # Selenium find header <h3> tag for every position
        try:
            seo_title = position.find_element(By.TAG_NAME, 'h3').text
        except:
            seo_title = ''

        # Selenium find link <a> tag for every position    
        try:
            seo_link = position.find_element(By.TAG_NAME, 'a')
            seo_link_href = seo_link.get_attribute('href')
            seo_link_parsed = urlparse(seo_link_href)
            seo_link_parsed_hostname = seo_link_parsed.hostname
        except:
            seo_link_href = ''

        # Selenium find span <span> tag with description for every position
        try:
            seo_description_container = position.find_element(By.CLASS_NAME, 'VwiC3b')
            seo_description = seo_description_container.find_element(By.TAG_NAME, 'span').text
        except:
            seo_description = ''
        
        
        # arr to exclude websites from top positions
        arr_exclude = ['twitter.com', 'www.instagram.com', 'www.google.cl', 'www.google.com', 'play.google.com', 'www.oddschecker.com']

        # Check data to append it to main arr_return
        if seo_title != '' and seo_link_parsed_hostname not in arr_exclude:

            position_object = {
                "position": f"{postion_counter}",
                "link": seo_link_href,
                "web": seo_link_parsed_hostname, 
                "title": seo_title,
                "description": seo_description
            }
            arr_return.append(position_object)

            postion_counter += 1
    wd.close()
    return arr_return