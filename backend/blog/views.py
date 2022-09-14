import re
from django.template import loader
from django.http import HttpResponse
from .models import Posts

posts = [
    {
        'author': 'hauvo@gmail.com',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 20118'
    },
        {
        'author': 'hauvo@gmail.com',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 20118'
    },
        {
        'author': 'hauvo@gmail.com',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'August 27, 20118'
    }
]

def home(request):
    template = loader.get_template('home.html')
    context = {
        'title': 'Blog Home',
        'posts': Posts.objects.all(),   
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html') 
    context = {
        'title': 'Blog About'
    }
    return HttpResponse(template.render(context, request))
