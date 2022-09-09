from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import render
from rest_framework import viewsets  
from .serializers import UsersSerializer 
from .models import Users

"""
@author <hauvo1709@gmail.com>
@todo:
@param request
@return 
"""
def list(request):
    template = loader.get_template('list.html')
    users = []
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))

class UsersView(viewsets.ModelViewSet):
    serializer_class = UsersSerializer   
    queryset = Users.objects.all()  
