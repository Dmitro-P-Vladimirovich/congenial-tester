from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_scroll(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    driver.execute_script('window.scrollTo(1, document.body.scrollHeight);')
    driver.execute_script('window.scrollTo(1, 500);')


def test_scroll_to_element(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    link = driver.find_element(By.LINK_TEXT, 'Бас-гитары со скидкой')
    driver.execute_script('arguments[0].scrollIntoView();', link)
    # ActionChains(driver).scroll_to_element(link).click(link).perform()


def test_upload(driver):
    driver.get('https://www.tutorialspoint.com/selenium/practice/upload-download.php')
    upload = driver.find_element(By.ID, 'uploadFile')
    upload.send_keys('C:/Users/1/Downloads/upsnd6g4fz4.jpg')




