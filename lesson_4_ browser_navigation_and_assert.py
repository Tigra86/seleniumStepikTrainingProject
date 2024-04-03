# Инициализировать драйвер (любой, попробуйте Firefox) p.s: не забудьте его установить.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открыть любую страницу, например: vk.com.
driver.get('https://www.google.com/')

# Получить и вывести title в консоль.
print(driver.title)

# Открыть любую другую страницу, например: ya.ru.
driver.get('https://www.instagram.com/')

# Получить и вывести title в консоль.
print(driver.title)

# Вернуться назад и, используя assert, убедиться, что вы точно вернулись обратно.
driver.back()
assert driver.current_url == 'https://www.google.com/'

# Сделать рефреш страницы.
driver.refresh()

# Получить и вывести URL-адрес текущей страницы.
print(driver.current_url)

# Вернуться "вперед" на страницу из пункта 4.
driver.forward()

# Убедиться, что URL-адрес изменился.
assert driver.current_url != 'https://www.google.com/'
