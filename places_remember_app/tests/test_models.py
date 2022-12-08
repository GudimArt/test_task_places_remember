from django.test import TestCase, Client
from places_remember_app.models import Memory


class TestModels(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            password='12345')
        self.user.save()
        self.memory = Memory.objects.create(
            title='MyTitle',
            description='Это чудесное место',
            address='Красноярск',
            owner=self.user,
        )
        self.memory.save()

    def tearDown(self):
        self.user.delete()
        self.memory.delete()
