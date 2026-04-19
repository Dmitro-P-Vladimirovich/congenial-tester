import requests

def all_posts():
    # get_all = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts') - Старый метод
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    # print(response.text) - Все данные текстом
    assert len(response) == 100, 'Not all posts returned'


def get_by_id():
    post_id = new_post()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    assert response['id'] == post_id, 'id is not correct'



def create_post():
    body = {
        "title": "sasssss",
        "body": "kokkkkk",
        "userId": "dfgdfgdfg"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    assert response.status_code == 201, 'Status code is incorrect'
    assert response.json()['id'] == 101, 'ID is incorrect'



def new_post():   # Функция-предусловие для следующих тестов (get, put, patch, delete)
    body = {       # Функция не выполнится, т.к. в этой API не создаются новые посты
        "title": "sasssss",
        "body": "kokkkkk",
        "userId": "dfgdfgdfg"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    return response.json()['id']


def update_post():
    post_id = new_post()   # Результат предыдущей функции (айдишник нового поста)
    body = {
        "title": "bassssssss",
        "body": "precision",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['title'] == 'bassssssss'
    clear(post_id)


def clear(post_id):   # Функция-постусловие для тестов (put, patch, delete)
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


def update_title_and_user_id():
    post_id = new_post()
    body = {
        "title": "spasssssss",
        "userId": 666
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    ).json()
    print(response)
    clear(post_id)



def delete_post():
    post_id = new_post()
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(response.json())
    print(response.status_code)



get_by_id()