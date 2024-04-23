import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

PROXY = "202.62.10.210:8080"  # Указываем адрес прокси-сервера

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={PROXY}")  # Добавляем прокси через опции

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://whatismyipaddress.com/")  # Проверяем IP-адрес

time.sleep(5)
