import re
from django.template import loader
from django.http import HttpResponse
from .models import Posts

def home(request):
    template = loader.get_template('home.html')
    context = {
        'title': 'Blog Home',
        'posts': Posts.objects.using('mysql').all(),   
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html') 
    context = {
        'title': 'Blog About'
    }
    return HttpResponse(template.render(context, request))
