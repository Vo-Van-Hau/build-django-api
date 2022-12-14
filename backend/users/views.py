from rest_framework import viewsets  
from .serializers import UsersSerializer 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class UsersView(viewsets.ModelViewSet):
    serializer_class = UsersSerializer   
    queryset = User.objects.all() 


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


@login_required
def profile(request):
    template = loader.get_template('profile.html')
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated !!!')
            return redirect('profile')
        else:
            messages.warning(request, f'Your Account has been failed to update !!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'title': 'Your Profile',
        'u_form': u_form,
        'p_form': p_form,
    }
    return HttpResponse(template.render(context, request))
 

