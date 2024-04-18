#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver


#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import time

link = "https://selenium1py.pythonanywhere.com/"
asd
class TestMainPage1():
    @pytest.fixture
    def start_class(self):
        print("старт браузера")
        self.browser  = webdriver.Chrome()
    @pytest.fixture
    def teardown_class(self):
        print("закрытие браузера")
        self.browser.quit()
    
    def test_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_link_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR,'.basket-mini .btn-group > a')


class TestMainPage2():

    def start_class(self):
        print("старт браузера")
        self.browser  = webdriver.Chrome()
   
    def teardown_class(self):
        print("закрытие браузера")
        self.browser.quit()
    
    def test_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_link_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR,'.basket-mini .btn-group > a')








    

 