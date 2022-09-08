from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

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
