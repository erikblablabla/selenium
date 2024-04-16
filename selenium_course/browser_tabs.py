#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver


#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

import time
import math
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    btn = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
    btn.click()
    browser.switch_to.window(browser.window_handles[1])
    def calc(x):
        return str(math.log(abs(12*math.sin(x))))
    math_element = browser.find_element(By.CSS_SELECTOR,'[id="input_value"]')
    x = int(math_element.text)
    input_form = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input_form.send_keys(calc(x))
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
finally:
    time.sleep(10)
    browser.quit()