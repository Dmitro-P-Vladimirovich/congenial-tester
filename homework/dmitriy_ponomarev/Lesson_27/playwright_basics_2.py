from playwright.sync_api import Page, expect, BrowserContext, Dialog
from time import sleep
import re


def test_visible(page: Page):
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    apply_button = page.locator('[class="filter-apply-button-popup__inner"]')
    # expect(country).not_to_be_visible()
    expect(apply_button).to_be_hidden()
    page.locator('[for="fc0"]').click()
    expect(apply_button).to_be_visible()
    sleep(2)


def test_enabled_and_select_and_text(page: Page):
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    catalog_button = page.locator('[title="Взглянуть на наш Каталог"]')
    expect(catalog_button).to_be_enabled()
    expect(catalog_button).to_have_text('Каталог')
    expect(catalog_button).to_contain_text('ало')
    page.locator('.js-set-catalog-filter-stock-mode').select_option('Под заказ')
    sleep(3)


def test_value(page: Page):
    text = 'precision'
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    input_field = page.locator('[name="q"]')
    input_field.fill(text)
    expect(input_field, f'Input value is not {text}').to_have_value(text)


def test_sort_and_wait(page: Page):
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    first_bass = page.locator('.product-card__link').locator('nth=0')
    print(first_bass.inner_text())
    page.locator('.js-set-catalog-sort').select_option('price.desc')
    expect(page).to_have_url(re.compile('price.desc'))
    print(first_bass.inner_text())
    sleep(5)


def test_focused(page: Page):
    page.goto('https://www.google.com/webhp?hl=en&gbv=1')
    field = page.locator('[name="q"]')
    expect(field).to_be_focused()


def test_tabs(page: Page, context: BrowserContext):
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    link = page.get_by_role('link', name='Франшиза').first
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    expect(new_page).to_have_title('Франшиза SKIFMUSIC')
    new_page.close()
    page.get_by_role('link', name='Каталог').first.click()
    sleep(3)


def test_hover(page: Page):
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    catalog_button = page.get_by_title('Взглянуть на наш Каталог')
    pedals = page.get_by_text('Педали и процессоры эффектов')
    bass_pedals = page.get_by_text('Педали для бас-гитар')
    catalog_button.click()
    pedals.hover()
    bass_pedals.click()
    sleep(3)


def test_d_n_d(page: Page):
    page.goto('https://www.tutorialspoint.com/selenium/practice/droppable.php')
    drag_me = page.locator('#draggable')
    drop_here = page.locator('#droppable')
    drag_me.drag_to(drop_here)
    sleep(3)


def test_alert(page: Page):

    def cancel_alert(alert: Dialog):
        print(alert.message)
        print(alert.type)
        alert.dismiss()
    def fill_and_accept(alert: Dialog):
        alert.accept()
    page.on('dialog', cancel_alert)
    # page.on('dialog', lambda alert: alert.accept(prompt_text='мой текст'))
    page.goto('https://www.tutorialspoint.com/selenium/practice/alerts.php')
    page.locator('[onclick="myPromp()"]').click()
    sleep(3)
