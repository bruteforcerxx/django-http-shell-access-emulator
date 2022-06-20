from django.urls import path
from . import views


urlpatterns = [
    path('', views.sender, name='post'),
    path('get', views.reader, name='get'),
    path('candy', views.script, name='candy'),
    path('register', views.register, name='register'),
    path('reader', views.reader, name='reader'),
    path('send_command', views.send_command, name='send_command'),
    path('command_response', views.command_response, name='command_response'),
    path('read_command', views.read_command, name='read_command'),
    path('command_feedback', views.command_feedback, name='command_feedback'),
]
