from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from .models import Event, Participation, Participant
from django.contrib.auth.decorators import login_required


# Create your views here.
# def login(request):
#     _message = 'Please sign in'
#     template_name = 'app/login.html'
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None and user.is_active:
#             auth_login(request, user)
#             return render(request, 'app/login.html')
#         else:
#             _message = 'Invalid username or password, please try again.'
#     return render(request, template_name, context={'message': _message})


def home(request):
    template_name = 'app/home.html'
    events = Event.objects.all()
    return render(request, template_name, {"events": events})


@login_required
def event(request):
    template_name = 'app/event.html'
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        time = request.POST.get("time")
        location = request.POST.get("location")
        if request.user.staff:
            Event(name=title, location=location, time=time, description=description,
                  posted_by=request.user.staff).save()
    return render(request, template_name)


def login(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth_login(request, user)
            return render(request, 'app/event.html')
        else:
            _message = 'Invalid username or password, please try again.'
    template_name = 'app/login.html'
    return render(request, template_name)


def get_detail(request):
    template_name = 'app/detail.html'
    if request.method == 'POST':
        _id = request.POST.get('event')
        _event = Event.objects.get(id=_id)
        if request.POST.get("first_name"):
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            phone_number = request.POST.get("phone")
            participant = Participant(first_name=first_name, last_name=last_name, email=email,
                                      phone_number=phone_number)
            participant.save()
            Participation(participant=participant, event=_event).save()
    return render(request, template_name, {"event": _event})

# Create your views here.
