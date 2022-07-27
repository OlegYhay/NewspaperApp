from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from users.models import Users


class TestHomePage(TestCase):

    def test_home_page(self):
        url = '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_name_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignUpTest(TestCase):
    def setUp(self):
        self.user = 'oleg'
        self.email = '123@Mail.ru'

    def test_signup_page_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        responses = self.client.get(reverse('signup'))
        self.assertTemplateUsed(responses, 'signup.html')

    def test_signup_form(self):
        newuser = Users.objects.create(
            username=self.user,
            email=self.email,
        )

        self.assertEqual(Users.objects.all().count(), 1)
        self.assertEqual(Users.objects.get(pk=1).username, self.user)
        self.assertEqual(Users.objects.get(pk=1).email, self.email)
