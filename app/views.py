from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from .models import Event


# Create your views here.
def login(request):
    _message = 'Please sign in'
    template_name = 'app/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth_login(request, user)
            return render(request, 'app/login.html')
        else:
            _message = 'Invalid username or password, please try again.'
    return render(request, template_name, context={'message': _message})


def home(request):
    template_name = 'app/home.html'
    return render(request, template_name)


def event(request):
    template_name = 'app/event.html'
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        time = request.POST.get("time")
        location = request.POST.get("location")
        Event(name=title, location=location, time=time, description=description).save()
    return render(request, template_name)


# Create your views here.
