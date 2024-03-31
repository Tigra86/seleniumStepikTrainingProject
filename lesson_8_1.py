'''
Задание 1:

1. Заполнить все текстовые поля данными (почистить поля перед заполнением).
2. Проверить, что данные действительно введены, используя get_attribute() и assert.

Страница для выполнения задания: https://demoqa.com/text-box
'''

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://demoqa.com/text-box')

full_name = driver.find_element('xpath', '//input[@id="userName"]')
full_name.clear()
full_name.send_keys('Tigran')
assert full_name.get_attribute('value') == 'Tigran'
time.sleep(2)

email_name = driver.find_element('xpath', '//input[@id="userEmail"]')
email_name.clear()
email_name.send_keys('email')
assert email_name.get_attribute('value') == 'email'
time.sleep(2)

curr_adr = driver.find_element('xpath', '//textarea[@id="currentAddress"]')
curr_adr.clear()
curr_adr.send_keys('current address')
assert curr_adr.get_attribute('value') == 'current address'
time.sleep(2)

perm_adr = driver.find_element('xpath', '//textarea[@id="permanentAddress"]')
perm_adr.clear()
perm_adr.send_keys('perm address')
assert perm_adr.get_attribute('value') == 'perm address'
time.sleep(2)
