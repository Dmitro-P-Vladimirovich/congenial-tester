from playwright.sync_api import Page, expect
import re
from time import sleep


def test_first(page: Page):
    page.goto('https://skifmusic.ru/')
    search_field = page.get_by_role('combobox').first.locator('input').first
    search_field.fill('precision')
    search_field.press('Enter')
    expect(page).to_have_title(re.compile('^precision'))


def test_by_role(page: Page):
    page.goto('https://skifmusic.ru/')
    page.get_by_role('link', name='Наши магазины').first.click()
    sleep(2)
    page.get_by_role('link', name='Москва', exact=True).click()  # exact - полное совпадение


def test_by_text(page: Page):
    page.goto('https://skifmusic.ru/')
    page.get_by_text('Корзина').first.click()
    sleep(3)


def test_by_label(page: Page):
    page.goto('https://skifmusic.ru/')
    page.get_by_label('Поле для поиска').fill('precision')
    sleep(3)


def test_by_placeholder(page: Page):
    page.goto('https://skifmusic.ru/')
    field = page.get_by_placeholder('Поиск')
    field.press_sequentially('jazz bass', delay=500)
    sleep(1)
    field.press('Control+a')
    sleep(1)
    field.press('Backspace')
    sleep(3)


def test_by_alt_text(page: Page):
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    page.get_by_alt_text('Бас-гитара Squier by Fender Sonic Precision Bass 2-Color Sunburst').click()
    sleep(3)


def test_by_title(page: Page):
    page.goto('https://www.google.com/')
    page.get_by_title('Поиск').fill('сас')
    sleep(3)


def test_by_test_id(page: Page):
    page.goto('https://www.airbnb.ru/')
    page.get_by_test_id('structured-search-input-field-query').fill('Батуми')
    sleep(3)


def test_by_css_selector(page: Page):
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    page.locator('[for="fc2"]').click()
    sleep(2)
    page.locator('.js-filter-reset').click()
    sleep(3)


def test_by_xpath(page: Page):
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    page.locator('//*[@for="fc2"]').click()
    sleep(3)