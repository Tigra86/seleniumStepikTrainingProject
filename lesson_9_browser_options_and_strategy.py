from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
# chrome_options.page_load_strategy = "eager"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(options=chrome_options, service=service)
browser.implicitly_wait(5)

browser.get('https://www.google.com/')
