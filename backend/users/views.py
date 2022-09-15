from rest_framework import viewsets  
from .serializers import UsersSerializer 
from .models import Users
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

class UsersView(viewsets.ModelViewSet):
    serializer_class = UsersSerializer   
    queryset = Users.objects.all() 


def signup(request):
    # form = UserCreationForm()
    form = CustomUserCreationForm()
    template = loader.get_template('signup.html')
    context = {
        'title': 'Signup Form',
        'form': form
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # The newly created User using UserCreationForm() will set is_superuser and is_staff as False but is_active set to True.
            form.save(form)  
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, f'Account created for {username}!, you are now able to login !!!')
            return redirect('signin')
        else:
            messages.warning(request, 'The credentials is not valid')
            return redirect('signup')
    else:
        return HttpResponse(template.render(context, request))
 

