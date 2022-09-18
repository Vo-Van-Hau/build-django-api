from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Posts
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

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

class PostListView(ListView):
    model = Posts
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Posts
    template_name = 'posts/detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = 'posts/upsert.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Posts
    template_name = 'posts/upsert.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = 'posts/delete.html'
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


