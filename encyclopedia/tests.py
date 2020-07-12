from django.test import TestCase, Client

# Create your tests here.

class FrontEndTests(TestCase):

    # def setUp(self):

    def test_is_working(self):
        c = Client()
        response = c.get("/wiki/")
        self.assertEqual(response.status_code, 200)

    def test_enteries_not_empty(self):
        c = Client()
        response = c.get("/wiki/")
        self.assertNotEqual(response.context['entries'], [])

    # For python page testing
    def test_python_page_working(self):
        c = Client()
        response = c.get("/wiki/Python/")
        self.assertEqual(response.status_code, 200)

    def test_python_page_contents(self):
        c = Client()
        response = c.get("/wiki/Python/")
        self.assertNotEqual(response.context['contents'], '')

    