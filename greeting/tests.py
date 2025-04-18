from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class GreetingTest(TestCase):
    def setUp(self):
        self.client = Client()

    def testIndexPage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello World!')
        self.assertTemplateUsed(response, 'index.html')
    
class GreetingFunctionlaityTest(TestCase):
        def test_greeting(self):
            response = self.client.get(reverse('index'))
            self.assertEqual(response.context['greeting'], 'Hello World!')
       