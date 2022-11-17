# import libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def gootData(wd, type):
    time.sleep(1.5)
    # var to store results
    arr_rising_return = []
    arr_main_return = []

    # Selenium find pagination's text button on googleTrends related box
    try:
        how_many_results = wd.find_element(By.XPATH, f'//div[@id="{type}"]//parent::div//child::div[@class="pagination"]//child::span').text
        how_many_results_split = how_many_results.split()
        # Var created to store how many iterations need to obtain al related terms
        how_many_iterations =  ['0'] * int((int(how_many_results_split[-1]) / 5))
    except:
        how_many_iterations = []

    # Selenium get first related terms texts and store them on arr_rising_return
    # array which contains text results of the googleTrends related box
    arr_text = wd.find_elements(By.XPATH, f'//div[@id="{type}"]//parent::div//child::div[@class="label-text"]//child::span')

    for element in arr_text:
        arr_rising_return.append(element.text)

    # Call function gootButtonNext(n_iterations) to get push button next and store related term's data
    gootButtonNext(wd, type, how_many_iterations, arr_rising_return)

    # Selenium get selector to change from Rising to Main related terms
    rising_to_main_btn = wd.find_element(By.XPATH, f'//div[@id="{type}"]//parent::div//child::md-select')
    rising_to_main_btn.click()
    time.sleep(1.5)
    ActionChains(wd)\
        .send_keys(Keys.ARROW_DOWN)\
        .send_keys(Keys.ENTER)\
        .perform()
    
    # Selenium find pagination's text button on googleTrends related box
    try:
        how_many_results_main = wd.find_element(By.XPATH, f'//div[@id="{type}"]//parent::div//child::div[@class="pagination"]//child::span').text
        how_many_results_split_main = how_many_results_main.split()
        # Var created to store how many iterations need to obtain al related terms
        how_many_iterations_main =  ['0'] * int((int(how_many_results_split_main[-1]) / 5))
    except:
        how_many_iterations_main = []


    # Selenium get first related terms texts and store them on arr_main_return
    # array which contains text results of the googleTrends related box
    arr_text_main = wd.find_elements(By.XPATH, f'//div[@id="{type}"]//parent::div//child::div[@class="label-text"]//child::span')

    for element in arr_text_main:
        arr_main_return.append(element.text)

    # Call function gootButtonNext(n_iterations) to get push button next and store related term's data
    gootButtonNext(wd, type, how_many_iterations_main, arr_main_return)

    # Prepare object to return with 
    goot_data = {
        'rising': arr_rising_return,
        'main': arr_main_return
    }
    return goot_data

    
# Function aux to click the button next and save the data of related terms for every iteration
def gootButtonNext(wd_iteration, type_iteration, n_iterations, arr_return_iteration):
    for iteration in n_iterations:
        time.sleep(1.5)
        # Selenium find pagination's next button on googleTrends related box and CLICK it
        button_next = wd_iteration.find_element(By.XPATH, f'//div[@id="{type_iteration}"]//parent::div//child::div[@class="pagination"]//child::button[@aria-label="Next"]')
        button_next.click()
        time.sleep(0.5)

        # array which contains text results of the googleTrends related box
        arr_text_iteration = wd_iteration.find_elements(By.XPATH, f'//div[@id="{type_iteration}"]//parent::div//child::div[@class="label-text"]//child::span')

        for element in arr_text_iteration:
            arr_return_iteration.append(element.text)    






    
    


    