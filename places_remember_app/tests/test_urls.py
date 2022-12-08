from django.test import SimpleTestCase
from django.urls import reverse, resolve
from places_remember_app.views import home, add_memory


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_add_memory_url_resolves(self):
        url = reverse('add_memory')
        self.assertEquals(resolve(url).func, add_memory)
