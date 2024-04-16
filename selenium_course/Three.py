#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver


#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    # elements = browser.find_elements(By.CSS_SELECTOR,'[placeholder="Input your name"]')  
    # for i in elements:
    #     if i.get_attribute('required'):
    #         i.send_keys("ghbdtn")
    # buton = browser.find_element(By.TAG_NAME,'button')
    # buton.click()
    element = browser.find_element(By.TAG_NAME, 'input')
    element_check = element.get_attribute('placeholder')
    print(element_check)
    time.sleep(1)


    #находим элемент содержащитй текст
    welcome_text = browser.find_element(By.TAG_NAME, "h1")
    #запишем текст из h1 в переменную
    welcome = welcome_text.text
    
    #с помощью assert проверяю, что ожидаемый текст совпадает с текстом на странице
    assert "Congratulations! You have successfully registered!" == welcome
   
finally:
    time.sleep(5)
    browser.quit()




