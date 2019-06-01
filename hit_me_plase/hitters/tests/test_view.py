from django.test import TestCase

from ..models import Hitter


class LandingPageViewTest(TestCase):
    def test_should_have_form_with_have_email_field_and_submit_button(self):
        response = self.client.get('/')

        expected = '<h1>Hit Me please!</h1>'
        self.assertContains(response, expected, status_code=200)

        expected = '<form action="." method="post">'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="hidden" name="csrfmiddlewaretoken"'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="email" name="email">'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="submit" value="Submit" />'
        self.assertContains(response, expected, status_code=200)

    def test_should_save_email_when_submit_form(self):
        data = {'email': 'fake_email@gmail.com'}

        response = self.client.post('/', data=data)

        self.assertEqual(response.status_code, 200)
        expected = Hitter.objects.filter(email=data['email']).count()
        self.assertEqual(expected, 1)
