import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, "
                            "like Gecko) Version/9.0.2 Safari/601.3.9")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://hyperskill.org/login")

"""
# Клик по кнопке, которая открывает новую вкладку
FOR_BUSINESS_BUTTON = ("xpath", "//a[text()=' For Business ']")
driver.find_element(*FOR_BUSINESS_BUTTON).click()
time.sleep(3)

current_tab = driver.current_window_handle
print(current_tab)

windows_count = driver.window_handles  # Записываем список открытых окон в переменную
print(len(windows_count))  # Выводим на экран кол-во открытых окон/вкладок

# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Открытие нескольких вкладок
driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
time.sleep(2)

# Шаг 3 - Получение списка открытых вкладок
windows = driver.window_handles
print(len(windows))  # Выведем на экран кол-во открытых вкладок

# Шаг 4 - Получение дескриптора текущего окна для дальнейшей проверки
current_tab = driver.current_window_handle
print("Дескриптор текущей вкладки: ", current_tab)
print("Индекс: ", windows.index(current_tab))  # Получаем индекс вкладки в списке для информативности

# Шаг 5 - Переключение на вкладку по ее индексу
driver.switch_to.window(windows[1])
time.sleep(2)

# Шаг 6 - Проверка, что вкладка переключилась
assert current_tab != driver.current_window_handle, "Вкладка не переключилась"
"""

"""
# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Получение дескриптора текущего окна
old_window = driver.current_window_handle
print("Дескриптор первого окна: ", old_window)

# Шаг 3 - Открытие и переключение на новое окно
driver.switch_to.new_window("window")

# Шаг 4 - Получение дескриптора нового окна
new_window = driver.current_window_handle
print("Дескриптор второго окна: ", new_window)

# Шаг 5 - Проверка, что окно переключилось
assert new_window == driver.current_window_handle, "Окно не переключилось"
time.sleep(2)

# Шаг 6 - Открытие страницы в новом окне
driver.get("https://vk.com")

# Шаг 7 - Переключение на старое окно
driver.switch_to.window(old_window)

# Шаг 8 - Проверка, что переключились на старое окно
assert old_window == driver.current_window_handle, "Окно не переключилось"

# Шаг 9 - Открытие страницы в старом окне
driver.get("https://ya.ru")

# Шаг 10 - Переключение на новое окно
driver.switch_to.window(new_window)

# Шаг 11 - Закрытие нового окна
driver.close()
"""

"""
Самостоятельная работа
1. Открыть 3 вкладки
2. Во вкладках перейти на страницы ниже страницы:
--Вкладка 1 - https://hyperskill.org/login
--Вкладка 2 - https://www.avito.ru/
--Вкладка 3 - https://www.ozon.ru/
3. Вывести в терминал title каждой страницы
4. Кликнуть на любую кнопку или ссылку на каждой странице

Важно:
--Сначала нужно открыть все 3 вкладки
--Потом получить все title страниц
--Потом кликнуть на любой элемент в каждой вкладке
Вариант, когда открыл вкладку получил title и кликнул, потом открыл новую вкладку получил title и кликнул, не подойдет. 
Важно походить по вкладкам.
"""


def test_new_tabs():
    driver.get("https://hyperskill.org/login")

    driver.switch_to.new_window("tab")
    driver.get("https://google.com")

    driver.switch_to.new_window("tab")
    driver.get("https://google.com")

    tabs = driver.window_handles
    for tab in tabs:
        driver.switch_to.window(tab)
        print("")
        print(driver.title)

    driver.switch_to.window(tabs[0])
    driver.find_element('xpath', '//*[@id="nav-collapse"]/div/ul[1]/li[2]/a').click()
    time.sleep(2)

    driver.switch_to.window(tabs[1])
    time.sleep(2)

    driver.switch_to.window(tabs[2])
    time.sleep(2)
