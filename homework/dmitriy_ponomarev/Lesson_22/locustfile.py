from locust import task, HttpUser
import random


class BookingUser(HttpUser):
    token = None


    def on_start(self):
        response = self.client.post(
            '/auth',
            json={'username': 'admin', 'password': 'password123'}
        )
        self.token = response.json()['token']


    @task(1)
    def patch_booking(self):
        body = {'firstname': 'Dennis', 'lastname': 'White'}
        headers = {'Cookie': f'token={self.token}'}
        self.client.patch(f'/booking/{random.choice([11, 12, 13, 14])}',
                          json=body, headers=headers)

    @task(2)
    def get_all_booking(self):
        self.client.get('/booking')

    @task(3)
    def get_booking_by_id(self):
        self.client.get(f'/booking/{random.choice([11, 12, 13, 14])}')
