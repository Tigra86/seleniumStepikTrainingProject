import os
import time
import pickle

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
import platform

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, "
                            "like Gecko) Version/9.0.2 Safari/601.3.9")

service = Service(ChromeDriverManager().install())

os_name = platform.system()
cmd_ctrl = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL

driver = webdriver.Chrome(service=service, options=chrome_options)


def test_dropdowns_old_style():
    driver.get("http://the-internet.herokuapp.com/dropdown")

    DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")
    DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))

    # Выбор элемента по содержимому text
    DROPDOWN.select_by_visible_text("Option 2")

    # Выбор элемента по index
    DROPDOWN.select_by_index(2)

    # Выбор элемента по value
    DROPDOWN.select_by_value("2")


def test_dropdowns_loop_through_options():
    driver.get("https://demoqa.com/select-menu")

    DROPDOWN_LOCATOR = ("xpath", "//select[@id='oldSelectMenu']")

    DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR))

    all_options = DROPDOWN.options  # Запишем все элементы выпадающего списка

    for option in all_options:  # Перебор элементов по тексту
        time.sleep(1)
        DROPDOWN.select_by_visible_text(option.text)

    for option in all_options:  # Перебор элементов по индексу
        time.sleep(1)
        DROPDOWN.select_by_index(all_options.index(option))

    for option in all_options:  # Перебор элементов по value
        time.sleep(1)
        DROPDOWN.select_by_value(option.get_attribute("value"))


def test_drovdowns_keyboard():
    driver.get("http://the-internet.herokuapp.com/key_presses")  # Сайт для работы

    KEY_PRESS_INPUT = ("xpath", "//input[@id='target']")  # Поле ввода

    driver.find_element(*KEY_PRESS_INPUT).send_keys("Hello World")  # Ввод текста

    driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.COMMAND + "A")  # Выделение всего текста

    driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.BACKSPACE)  # Удаление выделенного текста


def test_copy_paste():
    driver.get("https://clipboardjs.com/")

    COPY_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
    PASTE_LOCATOR = ("xpath", "//textarea[@id='bar']")

    COPY = driver.find_element(*COPY_LOCATOR)
    PASTE = driver.find_element(*PASTE_LOCATOR)

    PASTE.send_keys(cmd_ctrl + "A")  # Выделим все внутри поля
    time.sleep(2)
    PASTE.send_keys(cmd_ctrl + "X")  # Вырежем весь текст
    time.sleep(2)
    PASTE.send_keys(cmd_ctrl + "V")  # Вставим весь текст


def test_dropdowns_new_style():
    # Option 1
    driver.get("https://demoqa.com/select-menu")

    SELECT_TITLE = ("xpath", "//input[@id='react-select-3-input']")  # Локатор нашего dropdown

    driver.find_element(*SELECT_TITLE).send_keys("Mrs.")  # Вводим текст в dropdown
    time.sleep(5)
    driver.find_element(*SELECT_TITLE).send_keys(Keys.ENTER)

    # Option 2.1
    driver.get("https://demoqa.com/select-menu")
    driver.find_element("xpath", "//div[@id='withOptGroup']").click()  # Открываем dropdown
    driver.find_element("xpath",
                        "//div[@id='withOptGroup']//div[text()='A root option']").click()  # Кликаем на элемент внутри

    # Option 2.1
    driver.get("https://demoqa.com/select-menu")

    driver.find_element("xpath", "//div[@id='withOptGroup']").click()  # Открываем dropdown

    def choose_dropwdown_element_by_text(text):  # Будем искать элемент внутри dropdown по тексту
        elements = driver.find_elements("xpath", "//div[@id='withOptGroup']//div[contains(@id, 'react-select')]")
        for element in elements:
            if text in element.text:
                return element  # Возвращаем нужный элемент из dropdown по тексту

    choose_dropwdown_element_by_text("Another root option").click()  # Кликаем на выбранный элемент
