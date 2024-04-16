#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver


#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


import time
import math


link = "https://easysmarthub.ru/contact/"


try:
    browser = webdriver.Chrome()
    browser.get(link)
   
    input_1 = browser.find_element(By.NAME, "your-name")
    input_1.send_keys("Erik Spichak")
    input_2 = browser.find_element(By.NAME, "your-email")
    input_2.send_keys("Erikspichak@gmail.com")
    input_2 = browser.find_element(By.NAME, "your-subject")
    input_2.send_keys("3")
    input_2 = browser.find_element(By.NAME, "your-message")
    input_2.send_keys("Erikspichak@gmail.com")
    checkbox = browser.find_element(By.NAME, 'gdpr')
    checkbox.click()
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    



finally:
    time.sleep(12)
    #закрывает браузер после всех манипуляций даже если была ошибка
    browser.quit()
    