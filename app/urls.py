from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('event', views.event, name='event'),
    path('detail', views.get_detail, name='detail'),
]
