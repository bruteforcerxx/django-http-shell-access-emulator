from django.urls import path
from . import views


urlpatterns = [
    path('', views.sender, name='post'),
    path('get', views.reader, name='get'),
]
