import requests
from threading import Thread
import time
import json
import os

endpoint_2 = 'http://127.0.0.1:8000/'
endpoint_1 = 'https://xremote.herokuapp.com/'




def os_command():
    print('Anon-uit command line [Version 0.0.1]/Starting root command access...')
    while True:
        endpoint = f'{endpoint_1}send_command'
        command = input('Anon-uit command line [Version 0.0.1]/Enter command: ')
        content = {"command": command}
        sender = requests.post(endpoint, json=content)
        print(sender.json())


def message():
    while True:
        content = input('Anon-uit command line [Version 0.0.1]/Enter message: ')
        content = {"message": content}
        sender = requests.post(endpoint_1, json=content)
        print(sender.json())


def receiver():
    print('Anon-uit command line [Version 0.0.1]/Starting receiver...')
    while True:
        message = requests.get(f'{endpoint_1}command_response')
        message = dict(message.json())
        if message['new']:
            sender = message['sender']
            message = message['response']['response']

            print('')
            print('')
            print('\\-------------------------RECEIVE-RESPONSE---------------------------------')
            print(f'Anon-uit command output [Version 0.0.1]/From {sender}: {message}')
            print('-------------------------END-RESPONSE---------------------------------')
            print('')
            print('')

            print('\\Anon-uit command line [Version 0.0.1]/Enter command: ')


t1 = Thread(target=os_command)
t2 = Thread(target=receiver)
t1.start()
t2.start()

