from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import HomeWelcome


def index(request):
    mywelcome = HomeWelcome.objects.all().values()
    template = loader.get_template('HomeWelcome.html')
    context = {
        'mywelcome': mywelcome,
    }
    return HttpResponse(template.render())
# Create your views here.
mywelcome = HomeWelcome.objects.all().values()
print(mywelcome)