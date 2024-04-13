import os
import time
import pickle
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, "
                            "like Gecko) Version/9.0.2 Safari/601.3.9")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)


# Задание 1 (Установка и чтение куки)
def test_add_cookie():
    driver.get('https://google.com')

    driver.add_cookie({
        "name": "tigran",
        "value": "azaryan"
    })

    print("")
    print(driver.get_cookie("tigran"))


# Задание 2 (Замена куков)
def test_replace_cookie():
    driver.get('https://sharks1991club.com/')

    print("")
    print(driver.get_cookie("sbjs_current_add"))

    driver.delete_cookie("sbjs_current_add")
    driver.refresh()
    driver.add_cookie({
        "name": "sbjs_current_add",
        "value": "tigran"
    })

    print("")
    print(driver.get_cookie("sbjs_current_add"))


# Задание 3 (Автоматизация корзины покупок)
def test_amazon_cart():
    driver.get(
        'https://www.amazon.com/Marvel-Encyclopedia-New-Stan-Lee/'
        'dp/0241357551/ref=tmm_hrd_swatch_0?_encoding=UTF8&qid=&sr=')

    # *In case you don't have cookies saved
    # Add item to the cart and save all cookies
    # ADD_TO_CART_BTN = ('xpath', '//input[@id="add-to-cart-button"]')
    # driver.find_element(*ADD_TO_CART_BTN).click()

    # pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

    # Delete all cookies
    driver.delete_all_cookies()

    # Create a list with all cookies, loop through it, add previously saved cookies, one by one and refresh the page
    cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

    time.sleep(3)
