#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver


#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/get_attribute.html?ruler=robots")
    element = browser.find_elements(By.ID,'treasure')
    element_img_att = element.get_attribute('width')
    print(element_img_att)  
    
   
finally:
    time.sleep(5)
    browser.quit()




