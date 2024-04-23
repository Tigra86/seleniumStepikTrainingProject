"""
Сайт для выполнения задания: https://demoqa.com/selectable
1. Открыть вкладку Grid
2. Кликнуть на пару любых элементов
3. Убедиться, что они выбраны
4. Кликнуть еще раз и убедиться, что теперь они не выбраны
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, "
                            "like Gecko) Version/9.0.2 Safari/601.3.9")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)


def test_checkboxes_radio_btns():
    driver.get('https://demoqa.com/selectable')

    GRID_TAB = ('xpath', '//a[@id="demo-tab-grid"]')
    driver.find_element(*GRID_TAB).click()

    # Find all checkboxes, click on all of them, and verify that all checkboxes are selected
    checkboxes = driver.find_elements('xpath', '//div[@id="gridContainer"]//li')
    for checkbox in checkboxes:
        checkbox.click()
        assert 'active' in checkbox.get_attribute('class'), 'One or more checkboxes are not selected'

    # Deselect all checkboxes and verify that all checkboxes are deselected
    for checkbox in checkboxes:
        checkbox.click()
        assert 'active' not in checkbox.get_attribute('class'), 'One or more checkboxes are still selected'
