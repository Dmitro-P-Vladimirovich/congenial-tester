from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.implicitly_wait(10)
    # sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_clear(driver):
    input_data = 'precision'
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    text_string = driver.find_element(By.ID, 'instant-search-input')
    text_string.send_keys(input_data)
    sleep(2)
    entered_value = text_string.get_attribute('value')
    # text_string.clear()
    for _ in range(len(entered_value)):
        text_string.send_keys(Keys.BACKSPACE)
    assert text_string.is_displayed()


def test_enabled_and_select(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Взглянуть на наш Каталог"]')
    print(button.is_enabled())
    select = driver.find_element(By.CLASS_NAME, 'js-set-catalog-filter-stock-mode')
    dropdown = Select(select)
    dropdown.select_by_value('preorder')


def test_implicitly_wait(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    button_support = driver.find_element(By.ID, 'supportTrigger')
    button_support.click()


def test_web_drive_wait(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    wait = WebDriverWait(driver, 10)
    button_support = wait.until(EC.element_to_be_clickable((By.ID, 'supportTrigger')))
    button_support.click()
    driver.add_cookie({'name': 'testname', 'value': 'testvalue'})
    print(driver.get_cookies())


def test_same_elements(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    product_link = driver.find_elements(By.CLASS_NAME, 'product-card__link')
    print(product_link[0].text)
    print(product_link[-1].text)


def test_same_cards(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    product_cards = driver.find_elements(By.CLASS_NAME, 'product-card')
    for card in product_cards:
        print(card.find_element(By.CLASS_NAME, 'product-card__price').text)
    # print(product_cards[0].find_element(By.CLASS_NAME, 'product-card__price').text)




def test_wishlist(driver):
    driver.get('https://skifmusic.ru/product/617125-jet-jjb-300-vyw-bas-gitara-4-struny')
    button_add_to_wishlist = driver.find_element(By.CLASS_NAME, 'js-product-toggle-wishlist')
    button_add_to_wishlist.click()
    counter = driver.find_element(By.CSS_SELECTOR, '.user-nav__item--favorites')
    assert counter.get_attribute('data-quantity') == '1'


