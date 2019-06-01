from django.shortcuts import render
from django.views import View


class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'index.html'

        return render(request, template_name)
