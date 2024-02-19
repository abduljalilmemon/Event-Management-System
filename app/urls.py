from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.get_events, name='home'),
    path('/', views.get_events, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.custom_logout, name='logout'),
    path('event', views.create_event, name='event'),
    path('detail', views.get_detail, name='detail'),
    path('import-events', views.import_events, name='import-events'),
    path('my-event', views.get_my_event, name='my-event'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
