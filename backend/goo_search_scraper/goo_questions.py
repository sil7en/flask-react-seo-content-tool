from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Function to obtain related questions from Google, starting from one query, using Selenium webdriver
# Función para obtener las preguntas relacionadas a partir de una query con Selenium wd
def gooQuestions(wd):
  arr_return_questions = []
  #wd.maximize_window()
  # Selenium scroll down on the page simulating keyboard action
  wd.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
  time.sleep(0.5)

  try:
      goo_question_click = wd.find_element(By.XPATH, '//div[@jsname="Cpkphb"]//child::div[@jsname="tJHJj"]')
      time.sleep(0.75)
  except:
      print('Except: can\'t find jsname Cpkphb')

  try:
      goo_question_click.click()
      time.sleep(0.5)
  except:
      print('Except: can\'t click over question')

  try:
      goo_questions_click = wd.find_elements(By.XPATH, '//div[@jsname="Cpkphb"]//child::div[@jsname="tJHJj"]')
      time.sleep(0.75)
  except:
      print('Except: can\'t find jsname Cpkphb')

  for element in goo_questions_click[1:]:
      try:
          element.click()
          time.sleep(0.5)
      except:
          print('Except: can\'t click over question')

  time.sleep(0.75)

  # Second iteration
  try:
      goo_questions_click = wd.find_elements(By.XPATH, '//div[@jsname="Cpkphb"]//child::div[@jsname="tJHJj"]')
      time.sleep(0.75)
  except:
      print('Except: can\'t find jsname Cpkphb')

  for element in goo_questions_click[1:]:
      try:
          element.click()
          time.sleep(0.5)
      except:
          print('Except: can\'t click over question')

  time.sleep(0.75)

  google_related_questions = wd.find_elements(By.XPATH, '//div[@jsname="Cpkphb"]//child::div[@jsname="tJHJj"]')

  try:
      arr_textos_q = [element.find_element(By.XPATH, './/span').text for element in google_related_questions]
      arr_goo_related_questions = [element for element in arr_textos_q if element != '']
      arr_return_questions.extend(arr_goo_related_questions)
  except:
      print('Except: can\'t find related questions')
  google_search = wd.find_element(By.NAME, 'q')
  time.sleep(0.35)
  google_search.clear()
  wd.close()
  return arr_return_questions