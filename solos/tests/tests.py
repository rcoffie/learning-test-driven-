from django.test import TestCase
from django.urls import reverse, resolve
from solos.views import index
# Create your tests here.


class SolosURLsTestCase(TestCase):
    def test_root_url_uses_index_view(self):
        root = resolve('/')
        self.assertEqual(root.func, index)
