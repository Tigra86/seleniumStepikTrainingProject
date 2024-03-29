import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://google.com')
time.sleep(5)

driver.get('https://instagram.com')
time.sleep(5)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)

driver.refresh()