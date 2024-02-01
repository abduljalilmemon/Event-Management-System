from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render


# Create your views here.
def login(request):
    _message = 'Please sign in'
    a = 'app/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth_login(request, user)
            return render(request, 'app/login.html')
        else:
            _message = 'Invalid username or password, please try again.'
    return render(request, a, context={'message': _message})

# Create your views here.
