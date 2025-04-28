from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
# Create your views here.
from .models import User

def home(request):
    return render(request, 'bmqa1/home.html', {'name': ' Guest User'})

def registration(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            user = User(name=name, email=email, password=password)
            user.save()
            # fm = RegistrationForm()
            return render(request, 'bmqa1/success.html')
        else:
            return render(request, 'bmqa1/registration.html', {'form': fm})
    else:
        fm = RegistrationForm()
    return render(request, 'bmqa1/registration.html', {'form': fm})

def login(request):
    if request.method == 'POST':
        fm = LoginForm(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            users = User.objects.all()
            # print(user.name)
            for user in users:
                if user.email == email and user.password == password:
                    print(user.name)
                    request.session['user_name'] = user.name
                    return redirect('/bmqa1/profile')
            return render(request, 'bmqa1/login.html', {'form': fm, 'error': 'Invalid credential, try again.'})
    else:
        fm = LoginForm()
    return render(request, 'bmqa1/login.html', {'form': fm})

def profile(request):
    user_name = request.session.get('user_name', 'Guest')
    # print(user_name)
    return render(request, 'bmqa1/profile.html', {'name': user_name})

def success(request):
    return render(request, 'bmqa1/success.html',)

