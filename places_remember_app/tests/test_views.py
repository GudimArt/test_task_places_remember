from django.test import TestCase, Client
from django.urls import reverse
from places_remember_app.models import Memory
from django.contrib.auth.models import User
from django.contrib.auth import get_user
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.add_memory_url = reverse('add_memory')
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'places_remember_app/home.html')

    def test_home_if_auth_GET(self):
        logged_in = self.client.login(username='testuser', password='12345')
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'places_remember_app/home.html')

    def test_add_memory_if_not_auth_POST(self):
        response = self.client.post(self.add_memory_url,
                                    {
                                        'title': 'MyTitle',
                                        'description': 'Это чудесное место',
                                        'address': 'Красноярск',
                                    })
        self.assertEquals(response.status_code, 200)

    def test_add_memory_if_auth_POST(self):
        logged_in = self.client.login(username='testuser', password='12345')
        response = self.client.post(self.add_memory_url,
                                    {
                                        'title': 'MyTitle',
                                        'description': 'Это чудесное место',
                                        'address': 'Красноярск',
                                    })
        self.assertEquals(response.status_code, 302)

    def test_del_memory_if_not_auth_DELETE(self):
        memory1 = Memory.objects.create(
            title='MyTitle',
            description='Это чудесное место',
            address='Красноярск',
            owner=self.user
        )
        del_memory = reverse('del_memory', kwargs={'id': 1})
        response = self.client.delete(
            del_memory)
        self.assertEquals(response.status_code, 200)

    def test_del_memory_memory_if_auth_DELETE(self):
        memory1 = Memory.objects.create(
            title='MyTitle',
            description='Это чудесное место',
            address='Красноярск',
            owner=self.user
        )
        del_memory = reverse('del_memory', kwargs={'id': 1})
        logged_in = self.client.login(username='testuser', password='12345')
        response = self.client.delete(
            del_memory)
        self.assertEquals(response.status_code, 302)
