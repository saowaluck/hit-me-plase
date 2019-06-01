from django.http import HttpResponse
from django.views import View


class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        html = '<form action="" method="post">' \
            '<input type="email" name="email">' \
            '<input type="submit" value="Submit" />' \
            '</form>'
        return HttpResponse(html)
