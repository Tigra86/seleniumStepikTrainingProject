from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, "
                            "like Gecko) Version/9.0.2 Safari/601.3.9")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://testautomationpractice.blogspot.com")

iframe_volunteer = driver.find_element("xpath", "//iframe")

driver.switch_to.frame(iframe_volunteer)

first_name_field = driver.find_element("xpath", "//input[@name='RESULT_TextField-0']")
first_name_field.send_keys("Alexey")

driver.switch_to.default_content()  # Переключение с iframe обратно на страницу
