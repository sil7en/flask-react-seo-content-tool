from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to obtain related keywords starting from one query, using Selenium webdriver
# Función para obtener las keywords relacionadas a partir de una query con Selenium wd
def gooQueries(wd):
    wd.maximize_window()
    arr_return_goo_queries = []
    google_search = wd.find_element(By.NAME, 'q')
    google_search.click()
    time.sleep(0.75)
    google_related_searchs = google_search.find_elements(By.XPATH, '//li[@class="sbct"]')
    arr_textos = [element.find_element(By.XPATH, './/span').text for element in google_related_searchs]
    arr_goo_related_querys = [element for element in arr_textos if element != '']
    arr_return_goo_queries.extend(arr_goo_related_querys)
    time.sleep(0.05)
    google_search.clear()
    return arr_return_goo_queries