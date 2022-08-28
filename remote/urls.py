from django.urls import path
from . import views


urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('', views.index, name='index'),
    path('terminal/<uid>', views.terminal, name='terminal'),
    path('map_view/<ip>', views.map_view, name='map_view'),
    path('commander', views.commander, name='commander'),
    path('notifier', views.notifier, name='notifier'),
    path('shortcuts', views.short_cuts, name='shortcuts'),
    path('client_command_response', views.client_command_response, name='client_command_response'),
    path('get_resp', views.get_resp, name='get_resp'),
    path('get', views.reader, name='get'),
    path('candy', views.script, name='candy'),
    path('login', views.login_cl, name='login'),
    path('get_uid', views.get_uid, name='get_uid'),
    path('get_clients', views.get_clients, name='get_clients'),
    path('reader', views.reader, name='reader'),
    path('ping', views.ping, name='ping'),
    path('send_command', views.send_command, name='send_command'),
    path('command_response', views.command_response, name='command_response'),
    path('read_command', views.read_command, name='read_command'),
    path('command_feedback', views.command_feedback, name='command_feedback'),
]
