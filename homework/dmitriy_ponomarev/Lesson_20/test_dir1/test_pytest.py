import requests
import pytest
import time
import allure


@pytest.fixture()
def new_post_id():
    body = {"title": "sasssss", "body": "kokkkkk", "userId": "666"}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('deleting the post')
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

@pytest.fixture(scope='session')
def hello():
    print('hello')
    yield
    print('Bye')


@allure.feature('Posts')
@allure.story('Get posts')
@pytest.mark.smoke
def test_get_by_id(new_post_id):
    print('test')
    with allure.step(f'Run get request for post with id {new_post_id}'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    with allure.step(f'Check that post_id is {new_post_id}'):
        assert response['11'] == new_post_id


@allure.feature('Posts')
@allure.story('Get posts')
@allure.title('Получить все посты')
@allure.issue('https://www.sports.ru/', 'GETNEW-88')
@pytest.mark.smoke
def test_get_all_posts(hello):
    print('test')
    with allure.step('Run get request for all posts'):
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    with allure.step(f'Check that number of posts equal 100'):
        assert len(response) == 100


@allure.feature('Posts')
@allure.story('Change posts')
@pytest.mark.regression
def test_add_post():
    print('test')
    with allure.step('Prepare test data'):
        body = {
            "title": "sasssss",
            "body": "kokkkkk",
            "userId": "dfgdfgdfg"
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Run request to create a post'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
    with allure.step('Check response code is 201'):
        assert response.status_code == 201
    with allure.step('Check id of create post is 101'):
        assert response.json()['id'] == 101


@allure.feature('Example')
@allure.story('equals')
@pytest.mark.regression
def test_one():
    # time.sleep(3)
    assert 1 == 1


@allure.feature('Example')
@allure.story('equals')
@pytest.mark.parametrize('logins', ['', '   ', '$%#%^&*', 666])
def test_two(logins):
    print(logins)
    assert 1 == 1


@allure.feature('Example')
@allure.story('equals')
def test_three():
    # time.sleep(3)
    assert 1 == 1