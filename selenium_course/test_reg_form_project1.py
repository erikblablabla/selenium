#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver


#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
import time
import unittest
import math




class RegTestForm(unittest.TestCase):
    def test_registration_form_on_valible(self):
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration1.html")
            

        finally:
            time.sleep(5)
            browser.quit()
    

    


if __name__ == "__main__":
    unittest.main()
