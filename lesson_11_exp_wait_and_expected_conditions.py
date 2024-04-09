'''
Самостоятельная работа
Сайт для выполнения работы:
https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver

1. Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом
2. Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”
3. Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”
4. Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта
Советы:
Выставите явное ожидание на 15 секунд
Для выполнения задания 4, провалитесь в библиотеку EC и поищите метод, погуглите и т.д
'''


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")


# 1. Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом
def test_change_text():
    CHANGE_TEXT_BTN = ("xpath", "//button[@id='populate-text']")
    driver.find_element(*CHANGE_TEXT_BTN).click()
    TEXT = ("xpath", "//h2[@id='h2']")
    wait.until(EC.text_to_be_present_in_element(TEXT, 'Selenium Webdriver'))


# 2. Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”
def test_display_button_after_seconds():
    DISPLAY_BTN = ("xpath", "//button[@id='display-other-button']")
    driver.find_element(*DISPLAY_BTN).click()
    HIDDEN_BTN = ("xpath", "//button[@id='hidden']")
    wait.until(EC.visibility_of_element_located(HIDDEN_BTN))


# 3. Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”
def test_enable_button_after_seconds():
    ENABLE_BTN = ("xpath", "//button[@id='enable-button']")
    driver.find_element(*ENABLE_BTN).click()
    DISABLE_BTN = ("xpath", "//button[@id='disable']")
    wait.until(EC.element_to_be_clickable(DISABLE_BTN))


# 4. Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта
def test_alert():
    ALERT_BTN = ("xpath", "//button[@id='alert']")
    driver.find_element(*ALERT_BTN).click()
    wait.until(EC.alert_is_present())
