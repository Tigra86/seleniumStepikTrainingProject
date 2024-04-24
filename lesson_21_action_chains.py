import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, "
                            "like Gecko) Version/9.0.2 Safari/601.3.9")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10, poll_frequency=1)  # Создаем обьект ожиданий
action = ActionChains(driver)  # создан обьект через который будут выполняться действия мыши

"""
driver.get("https://demoqa.com/buttons")

# Double click
DB_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")

BUTTON = driver.find_element(*DB_BUTTON_LOCATOR)

action.double_click(BUTTON).perform()

# Right button click
RС_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClickBtn']")

BUTTON = driver.find_element(*RС_BUTTON_LOCATOR)

action.context_click(BUTTON).perform()
"""

"""
# Hover the element
driver.get("https://demoqa.com/menu")

time.sleep(3)

STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

STEP_1 = driver.find_element(*STEP_1_LOCATOR)
STEP_2 = driver.find_element(*STEP_2_LOCATOR)
STEP_3 = driver.find_element(*STEP_3_LOCATOR)

action.move_to_element(STEP_1) \
    .move_to_element(STEP_2) \
    .pause(5) \
    .click(STEP_3) \
    .perform()
"""

"""
# Scroll to the element
driver.get("https://clipboardjs.com/")

SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")

SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)

action.scroll_to_element(SOME_ELEMENT).perform()  # Используем скролл до элемента

time.sleep(5)
"""
