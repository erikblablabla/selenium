#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver


#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

import time

import os

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")

    #Получяем путь к директории текущего исполняемого фйла
    input_1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input_1.send_keys('asd')
    input_2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"')
    input_2.send_keys('asd')
    input_3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_3.send_keys('asd')


    
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    # C:\Users\AuroraPC\Desktop\Selenium\selenium_course
    file_path = os.path.join(cur_dir, 'file.txt')
    # C:\Users\AuroraPC\Desktop\Selenium\selenium_course\file.txt
    # peremennaya = r"C:\Users\AuroraPC\Desktop\Selenium\selenium_course\file.txt"
    element = browser.find_element(By.CSS_SELECTOR,'[type="file"]')
    element.send_keys(file_path)

    btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn.click()

   

    # desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
    # file_path = os.path.join(desktop_path, "file.txt")
    # promt = browser.switch_to.alert
    # promt.send_keys("ваш отвте")
    # promt.accept() # принять
    # promt.dismiss() #отклонить

    
   
finally:
    time.sleep(5)
    browser.quit()




