from django.test import TestCase, RequestFactory
from solos.views import index
from django.db.models.query import QuerySet
from solos.models import Solo

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.drum_solo = Solo.objects.create(
        instrument = 'drums',
        artist = 'Rich',
        track = 'Bugle Call Rag'
        )

        self.base_solo = Solo.objects.create(
        instrument = 'saxophone',
        artist = 'Coltrane',
        track= 'Mr. PC'
        )

    def test_index_view_basic(self):
        request = self.factory.get('/')
        with self.assertTemplateUsed('solos/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)

    def test_index_view_returns_solos(self):
        response = self.client.get('/',{'instrument':'drums'})
        solos = response.context['solos']
        self.assertIs(type(solos),QuerySet)
        self.assertEqual(len(solos), 1)
        self.assertEqual(solos[0].artist, 'Rich')
