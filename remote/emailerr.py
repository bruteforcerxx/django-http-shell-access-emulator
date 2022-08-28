from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from ipware import get_client_ip
import geocoder
from .models import UserData
from django.contrib.auth.models import User
from os.path import exists
import os
from django.core.files.storage import FileSystemStorage
# Create your views here.


def report(context, request):
    ip, is_routable = get_client_ip(request)
    if ip is None:
        ips = geocoder.ip("me")
    else:
        if is_routable:
            ips = geocoder.ip(ip)
        else:
            ip = '172.20.10.6'
            ips = geocoder.ip("me")

    uid = context[6]
    user = User.objects.get(username=uid)
    client = UserData.objects.filter(user=user)
    if_new = UserData.objects.filter(ip=ip)
    new = False
    if len(if_new) < 1:
        new = True

    print(client)
    client = client[0]
    client.ip = ip
    print(f'clients ip is: {client.ip}')
    uid = client.uid
    client.save()

    all_visit = UserData.objects.all()
    x = float(len(all_visit))

    v_ip = f"System's IP: {ip}"
    v_uid = f"Sysyem's UID: {uid}"
    v_name = f"System's Name: {context[4]}"
    v_cwd = f"System's CWD: {context[5]}"
    v_country = f"System's Country: {ips.country}"
    v_city = f"System's City: {ips.city}"
    v_fre = f"New System: {new}."
    sys_num = f"Number of systems: {x}."

    message_data = [v_ip, v_uid, v_name, v_cwd, v_country, v_city, v_fre, sys_num]

    context[0]['message_data'] = message_data
    context[0]['button_link'] = f'https://xxremote.herokuapp.com/map_view/{ip}'

    send_emailerr(context[0], context[1], context[2], context[3])


def send_emailerr(context, subject, destination, template):
    print('starting email sender....')
    html_message = render_to_string(template, context)
    plain_message = strip_tags(html_message)
    from_email = "Remote <olumichael2015@outlook.com>"
    destination = str(destination)
    print('sending email....')
    status = mail.send_mail(subject, plain_message, from_email, [destination], html_message=html_message,
                            fail_silently=True)
    print(f'sender finished, status = {status}')
    return status

