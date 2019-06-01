from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import Hitter


class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'index.html'

        return render(request, template_name)

    def post(self, request):
        email = request.POST.get('email')

        Hitter.objects.create(email=email)

        return HttpResponse()
