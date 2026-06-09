from playwright.sync_api import Page, expect, Request, Route, APIResponse
from time import sleep
import json
import re


def test_listen(page: Page):
    def print_request(request: Request):
        print('REQUEST:', request.post_data, request.url)
    # def print_response(response: Response):
    #     print('RESPONSE:', response.status)  *добавил ниже как lambda-функцию
    page.on('request', print_request)
    page.on('response', lambda response: print('RESPONSE:', response.url, response.status))
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    input_field = page.locator('#instant-search-input')
    input_field.fill('precision')
    input_field.press('Enter')
    sleep(3)


def test_catch_response(page: Page):
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    with page.expect_response('**search**') as response_event:
        input_field = page.locator('#instant-search-input')
        input_field.fill('precision')

    response = response_event.value
    expect(APIResponse(response)).to_be_ok()  # преобразуем в APIResponse для проверки API
    print(response.url)
    print(response.status)
    response_data = response.json()
    assert response_data[0] == {
        'label': 'Fender Player II Precision Bass',
        'type': 'СЕРИЯ',
        'url': 'https://skifmusic.ru/catalog/seriya-fender--player-ii-precision-bass-2843s',
        'image_url': 'https://skifmusic.ru/thumbs/91/87/270x270_1_normal_3fee8d75d90af9fc8e16cfcc49f5.webp'
    }


def test_change_response(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['usd_current'] = '666'
        body['temp'] = '69'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route('https://www.m24.ru/js/infoline/infoline.json', handle_route)
    page.goto('https://www.m24.ru/')
    page.locator('.b-search-button').click()
    sleep(10)


def test_change_request(page: Page):
    def change_req(route: Route):
        url = route.request.url
        print(url)
        url = url.replace('&price_to=30000', '')
        route.continue_(url=url)
    page.route(re.compile('https://skifmusic.ru/catalog/bas-gitaryi-14?'), change_req)
    page.goto('https://skifmusic.ru/catalog/bas-gitaryi-14')
    filter_checkbox = page.locator('[for="fc0"]')
    # button_filter = page.locator('.filter-apply-button-popup__button')
    filter_checkbox.click()
    # button_filter.click()
    sleep(10)




