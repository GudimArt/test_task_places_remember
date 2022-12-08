from django.test import SimpleTestCase
from places_remember_app.forms import AddMemoryFrom


class TestForms(SimpleTestCase):
    def test_expence_form_valid_data(self):
        form = AddMemoryFrom(data={
            'title': 'MyTitle',
            'description': 'Это чудесное место',
            'address': 'Красноярск',
        })
        self.assertTrue(form.is_valid())

    def test_expence_form_valid_data(self):
        form = AddMemoryFrom(data={})
        self.assertFalse(form.is_valid())
