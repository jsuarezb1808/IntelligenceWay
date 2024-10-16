from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class UrlTests(TestCase):

    def test_home_url(self):
        response = self.client.get(reverse('index'))  
        self.assertEqual(response.status_code, 200)