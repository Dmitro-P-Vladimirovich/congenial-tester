from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_new_tab(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    driver.find_element(By.LINK_TEXT, 'Франшиза').click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    assert driver.title == 'Франшиза SKIFMUSIC'
    driver.close()
    driver.switch_to.window(tabs[0])


def test_iframe(driver):
    driver.get('https://www.tutorialspoint.com/selenium/practice/frames.php')
    iframe = driver.find_element(By.CSS_SELECTOR, '[src="new-tab-sample.php"]')
    driver.switch_to.frame(iframe)
    button = driver.find_element(By.CLASS_NAME, 'logo-desktop')
    button.click()
    sleep(2)
    driver.switch_to.default_content()
    driver.find_element(By.CSS_SELECTOR, '[data-bs-target="#collapseThree"]').click()



def test_stale_exception(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    checkbox = driver.find_element(By.CSS_SELECTOR, '[for="fc0"]')
    checkbox.click()
    button = driver.find_element(By.CLASS_NAME, 'js-filter-apply-button-popup--submit')
    button.click()
    assert driver.current_url == 'https://skifmusic.ru/catalog/bas-gitaryi-14?price_to=30000'


def test_drop_menu(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    driver.find_element(By.CSS_SELECTOR, '[title="Взглянуть на наш Каталог"]').click()
    wait = WebDriverWait(driver, 5)
    pedals = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Педали и процессоры эффектов')))
    ActionChains(driver).move_to_element(pedals).perform()
    bass_pedals = driver.find_element(By.LINK_TEXT, 'Педали для бас-гитар')
    bass_pedals.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Педали эффектов для бас-гитар'


def test_drag_and_drop(driver):
    driver.get('https://www.tutorialspoint.com/selenium/practice/droppable.php')
    first = driver.find_element(By.ID, 'draggable')
    second = driver.find_element(By.ID, 'droppable')
    # ActionChains(driver).drag_and_drop(first, second).perform()
    actions = ActionChains(driver)
    actions.click_and_hold(first)
    actions.move_to_element(second)
    actions.release()
    actions.perform()


def test_open_in_new_tab(driver):
    driver.get('https://skifmusic.ru/catalog/bas-gitaryi-14')
    link = driver.find_element(By.LINK_TEXT, 'Контакты')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()


def test_alerts(driver):
    driver.get('https://www.tutorialspoint.com/selenium/practice/alerts.php')
    driver.find_element(By.CSS_SELECTOR, '[onclick="myDesk()"]').click()
    alert = Alert(driver)
    alert.dismiss()
