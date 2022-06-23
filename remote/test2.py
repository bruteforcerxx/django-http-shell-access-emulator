import requests
import os
from datetime import datetime


endpoint_1 = 'http://127.0.0.1:8000/'
uid = '03kw1cc'

def commands():
    message = requests.get(f'{endpoint_1}command_response')
    message = dict(message.json())
    if message['new']:
        for r in message['response']:
            sender = r['client']
            message = r['response']
            receipt = r['time_received']
            dur = r['exec_duration']

            print('')
            print('')
            print('-------------------------RECEIVED-RESPONSE---------------------------------')
            print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: CLIENT UID: {sender}| '
                  f'CLIENT SIDE TIME OF RECEIPT: {receipt}| EXECUTION DURATION: {dur} ')
            print('-------------------------RECEIVED-DATA---------------------------------')
            print(message)
            print('-----------------------------END-RESPONSE---------------------------------')
            print('')
            print('')



def test():
    cmm = 'test responnse'
    content = {'response': cmm, 'client': uid, 'time_received': '', 'exec_duration': ''}
    sender = requests.post(f'{endpoint_1}command_feedback', json=content)
    print(sender.json())


test()
commands()
