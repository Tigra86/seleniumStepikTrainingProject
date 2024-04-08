'''
Задание 1. С помощью цикла for скачать все файлы в папку lesson_6/downloads.
Страница для выполнения задания: http://the-internet.herokuapp.com/download

Задание 2. Загрузить любой файл в 'Choose File'.
Страница для выполнения задания: https://demoqa.com/upload-download
'''

import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.getcwd() + "/downloads"
}
chrome_options.add_experimental_option("prefs", prefs)

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(options=chrome_options, service=service)
browser.implicitly_wait(5)

browser.get("http://the-internet.herokuapp.com/download")

# Find all downloadable links and click on those
elements = browser.find_elements("xpath", "//div[@class='example']/a")

for element in elements:
    element.click()

browser.get("https://demoqa.com/upload-download")

# Find the Choose File button and upload a file
upload_btn = browser.find_element("xpath", "//input[@type='file']")

upload_btn.send_keys(f"{os.getcwd()}/downloads/code.png")
