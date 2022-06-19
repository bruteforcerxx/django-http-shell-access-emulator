from django.http import HttpResponse
from rest_framework import status
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail


@api_view(['GET', 'POST'])
def register(request):
    try:
        new_user = 'helloworld001'
        email = 'helloworld@gmail.com'
        password = '1111'
        info = User.objects.create_user(username=new_user, email=email, password=password)
        info.save()
        context = {}
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
        user_1 = 'helloworld001'
        user_2 = 'helloworld002'
        post = request.POST
        print(post)
        message = post

        print(message)
        context = {'mode': 'SANDBOX', 'message': message}
        return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def reader(request):
    try:
        user_2 = 'helloworld002'
        context = {}
        return Response(context, status=status.HTTP_200_OK)

    except Exception as e:
        context = {'error_message': e}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
