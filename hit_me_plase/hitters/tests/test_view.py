from django.test import TestCase


class LandingPageViewTest(TestCase):
    def test_should_have_form_with_have_email_field_and_submit_button(self):
        response = self.client.get('/')

        expected = '<form action="" method="post">'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="email" name="email">'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="submit" value="Submit" />'
        self.assertContains(response, expected, status_code=200)
