'''
На странице https://testautomationpractice.blogspot.com/

1. Найти иконку Wikipedia по имени класса
2. Найти поле ввода Wikipedia по id
3. Найти кнопку поиска Wikipedia по классу
4. Найти любой другой элемент на странице по тегу
'''

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://testautomationpractice.blogspot.com/')

driver.find_elements('class name', 'wikipedia-icon')

driver.find_element('id', 'Wikipedia1_wikipedia-search-input')

driver.find_elements('class name', 'wikipedia-search-button')

driver.find_element('tag name', 'h1')