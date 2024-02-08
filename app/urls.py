from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.custom_logout, name='logout'),
    path('event', views.event, name='event'),
    path('detail', views.get_detail, name='detail'),
    path('import_events', views.import_events, name='import_events'),
    path('my-event', views.get_my_event, name='my-event'),
]
