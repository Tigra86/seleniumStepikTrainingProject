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
# Click and hold left button
driver.get("https://demoqa.com/buttons")

OUTLINE_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")

BUTTON = driver.find_element(*OUTLINE_BUTTON_LOCATOR)

action.click_and_hold(BUTTON).perform()
"""

"""
# Drag and drop
driver.get("https://demoqa.com/droppable")

SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")

SOURCE = driver.find_element(*SOURCE_LOCATOR)
TARGET = driver.find_element(*TARGET_LOCATOR)

wait.until(EC.element_to_be_clickable(SOURCE))
action.drag_and_drop(SOURCE, TARGET).perform() # Перетаскивание

time.sleep(5)
"""

"""
# Drag and drop as a function
driver.get("https://demoqa.com/sortable")

SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")


def drag_and_drop(source, target):
    SOURCE = driver.find_element(*source)  # Находим source-элемент
    TARGET = driver.find_element(*target)  # Находим target-элемент
    wait.until(EC.element_to_be_clickable(SOURCE))  # Ждем кликабельности source-элемента
    action.drag_and_drop(SOURCE, TARGET).perform()  # Перетаскиваем


drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR)  # Использование функции
"""

"""
1. Нажимаем и удерживаем кнопку на перетаскиваемом элементе с помощью метода click_and_hold().
2. Ждем появления зоны для перетаскивания.
3. Перетаскиваем на нее элемент.
4. Отпускаем кнопку мыши - это как раз и является нашей главной темой, так как selenium в цепочке действий работает 
точно как человек, ему нужно передать не только нажатие, но и отпускание кнопки в явном виде).
"""


def test_action_chains():
    driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")

    source = driver.find_element("xpath", "//div[@class='grid__item'][7]")  # Что перетаскиваем
    target = driver.find_element("xpath", "//div[@class='drop-area__item'][2]")  # Куда перетаскиваем

    action.click_and_hold(source) \
        .pause(2) \
        .move_to_element(target) \
        .release() \
        .perform()
