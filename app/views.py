from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from .models import Event, Participation, Participant
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import csv
import io
from datetime import datetime
from django.http import HttpResponse
from .forms import ImportForm
from django.contrib.auth import logout
from django.shortcuts import redirect


def custom_logout(request):
    logout(request)
    return redirect('home')


def home(request):
    template_name = 'app/home.html'
    if request.method == 'GET':
        query = request.GET.get('search', '')
        events = Event.objects.filter(name__icontains=query)
        paginator = Paginator(events, 10)
        page = request.GET.get('page')
        try:
            paginated_data = paginator.page(page)
        except PageNotAnInteger:
            paginated_data = paginator.page(1)
        except EmptyPage:
            paginated_data = paginator.page(paginator.num_pages)
        return render(request, template_name,
                      {"events": paginated_data, "query": query, 'total': Event.objects.count()})
    events = Event.objects.all()[:10]
    return render(request, template_name, {"events": events, 'total': Event.objects.count()})


@login_required
def get_my_event(request):
    template_name = 'app/myevent.html'
    if request.method == 'GET':
        query = request.GET.get('search', '')
        events = Event.objects.filter(name__icontains=query, posted_by=request.user.staff)
        paginator = Paginator(events, 10)
        page = request.GET.get('page')
        try:
            paginated_data = paginator.page(page)
        except PageNotAnInteger:
            paginated_data = paginator.page(1)
        except EmptyPage:
            paginated_data = paginator.page(paginator.num_pages)
        return render(request, template_name,
                      {"events": paginated_data, "query": query, 'total': len(events)})
    events = Event.objects.filer(posted_by=request.user.staff)
    return render(request, template_name, {"events": events[:10], 'total': len(events)})


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
    form = ImportForm()
    return render(request, template_name, {'form': form})


def login(request):
    _message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth_login(request, user)
            return redirect('home')
        else:
            _message = 'Invalid username or password, please try again.'
    template_name = 'app/login.html'
    return render(request, template_name, {"message": _message})


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
            participant, created = Participant.objects.get_or_create(first_name=first_name, last_name=last_name,
                                                                     email=email, phone_number=phone_number)
            Participation.objects.get_or_create(participant=participant, event=_event)
    return render(request, template_name, {"event": _event})


@login_required
def import_events(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES.get('csv_file')
            if not csv_file.name.endswith('.csv'):
                return HttpResponse('File is not a CSV')
            events_added = 0
            file = csv_file.read().decode('utf-8')
            csv_reader = csv.DictReader(io.StringIO(file))
            for _event in csv_reader:
                title = _event.get('name')
                description = _event.get('description')
                time = _event.get('date')
                location = _event.get('location')
                if request.user.staff:
                    date_object = datetime.strptime(time, "%m/%d/%Y")
                    formatted_date = date_object.strftime("%Y-%m-%d %H:%M:%S")
                    new_event = Event.objects.get_or_create(name=title, location=location, time=formatted_date,
                                                            description=description, posted_by=request.user.staff)
                    # Handle image
                    # image_name = row.get('image', '')
                    # if image_name:
                    #     image_path = os.path.join('path/to/your/images', image_name)
                    #     if os.path.exists(image_path):
                    #         event.image.save(image_name, File(open(image_path, 'rb')))
                    #     else:
                    #         # Use default placeholder image
                    #         event.image = 'default_image.png'
                    #
                    events_added += 1
            return render(request, 'event.html', {'form': ImportForm()})
    return render(request, 'event.html', {'form': form})
