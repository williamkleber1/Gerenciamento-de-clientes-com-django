from django.test import TestCase
from django.urls import reverse


class PessoaViewTestCase(TestCase):

    def test_status_code_200(self):
        response = self.client.get(reverse('views'))
        self.assertEquals(response.status_code, 200)
