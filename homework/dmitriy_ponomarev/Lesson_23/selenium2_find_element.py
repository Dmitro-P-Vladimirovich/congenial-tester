from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_id_and_class_name(driver):
    input_data = 'precision'
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    text_string = driver.find_element(By.ID, 'instant-search-input')
    text_string.send_keys(input_data)
    # text_string.submit()
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.CLASS_NAME, 'page-header__title')
    print(result_text.text)
    print(result_text.get_attribute('innerText'))
    assert input_data in result_text.text.lower()


def test_name_and_tag_name(driver):
    input_data = 'jazz bass'
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    text_string = driver.find_element(By.NAME, 'q')
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.TAG_NAME, 'h1')
    print(result_text.text)
    assert input_data in result_text.text.lower()


def test_link(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    # contact_link = driver.find_element(By.LINK_TEXT, 'Контакты')
    contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Конта')
    contact_link.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Контакты'


def test_css_selector(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    # text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder="Поиск"]')
    text_string = driver.find_element(By.CSS_SELECTOR, '#instant-search-input')
    assert text_string.get_attribute('placeholder') == 'Поиск'


def test_xpath(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    text_string = driver.find_element(By.XPATH, '//*[@placeholder="Поиск"]')
    text_string.send_keys('music man')
    text_string.send_keys(Keys.ENTER)


def test_css_style(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    catalog_button = driver.find_element(By.XPATH, '//*[@title="Взглянуть на наш Каталог"]')
    assert catalog_button.value_of_css_property('background-color') == 'rgba(251, 188, 51, 1)'