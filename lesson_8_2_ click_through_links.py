'''
Задание 2:

1. Прокликать все ссылки со статус-кодами на странице, используя алгоритм перебора элементов.
2. После каждого клика возвращаться на стартовую страницу.

Страница для выполнения задания: http://the-internet.herokuapp.com/status_codes
'''

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://the-internet.herokuapp.com/status_codes')
links = driver.find_elements('xpath', '//li//a')
URLS = ['https://the-internet.herokuapp.com/status_codes/200',
        'https://the-internet.herokuapp.com/status_codes/301',
        'https://the-internet.herokuapp.com/status_codes/404',
        'https://the-internet.herokuapp.com/status_codes/500'
        ]

for link in links:
    link.click()
    for i in URLS:
        assert driver.current_url in URLS
    time.sleep(2)
    driver.back()
