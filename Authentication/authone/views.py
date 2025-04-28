from django.shortcuts import render
from .forms import UserRegForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def UserRegistration(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'User Created!!')
                print('user created')
        else:
            print(form.errors)
            return render(request, 'authone/userreg.html', {'form': form})
    form = UserRegForm()
    return render(request, 'authone/userreg.html', {'form': form})


def UserLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
            else:
                print('login failed')
        else:
            print(form.errors)
            return render(request, 'authone/userlogin.html', {'form': form})
    form = AuthenticationForm()
    return render(request, 'authone/userlogin.html', {'form': form})