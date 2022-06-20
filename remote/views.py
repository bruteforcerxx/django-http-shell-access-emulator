from django.http import HttpResponse
from rest_framework import status
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
import random
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from .models import Messages, Command, Script, CommandResponse


@api_view(['GET', 'POST'])
def register(request):
    try:
        data = JSONParser().parse(request)
        print(data)
        user = str(data['user'])
        pwd1 = '1111'
        info = User.objects.create_user(username=user, password=pwd1)
        info.save()

        user = User.objects.get(username=user)
        new = Messages(user=user)
        cm = Command(user=user)
        sc = Script(user=user)
        new.save()
        cm.save()
        sc.save()
        context = {'message': f'registered {user} successfully'}
        return Response(context, status=status.HTTP_200_OK)
    except Exception as e:
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
def login(request):
    try:
        context = {}
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

            user = 'helloworld002'
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

            user = 'helloworld002'
            user = User.objects.get(username=user)
            mess = Command.objects.get(user=user)
            command = mess.command

            command = eval(command)
            command.append(data)
            print(command)

            mess.command = command

            mess.save()
            context = {'mode': 'SANDBOX', 'command': f'command sent to {user}'}
            return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def read_command(request):
    try:
        user = 'helloworld002'
        user = User.objects.get(username=user)
        mess = Command.objects.get(user=user)
        count = mess.command_count
        command = mess.command

        command = eval(command)
        print(len(command))
        print(int(count))

        if int(count) < int(len(command)):
            new_command = command[int(len(command) - 1)]
            mess.command_count = len(command)
            mess.save()
            print(command)
            context = {'new': True, 'command': new_command, 'sender': str(user)}
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {'new': False, 'command': ''}
            return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def command_feedback(request):
    try:
        if request.method == 'GET':
            context = {'mode': 'SANDBOX'}
            return Response(context, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            data = JSONParser().parse(request)

            user = 'helloworld001'
            user = User.objects.get(username=user)
            mess = CommandResponse.objects.get(user=user)
            command = mess.command

            command = eval(command)
            command.append(data)
            print(command)
            mess.command = command
            mess.save()

            context = {'mode': 'SANDBOX', 'response': f'response sent to {user}'}
            return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def command_response(request):
    try:
        user = 'helloworld001'
        user = User.objects.get(username=user)
        mess = CommandResponse.objects.get(user=user)
        count = mess.command_count
        command = mess.command

        command = eval(command)
        print(len(command))
        print(int(count))

        if int(count) < int(len(command)):
            new_command = command[int(len(command) - 1)]
            mess.command_count = len(command)
            mess.save()
            print(command)
            context = {'new': True, 'response': new_command, 'sender': str(user)}
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {'new': False, 'command': ''}
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