import requests
import os
from datetime import datetime


endpoint_1 = 'http://127.0.0.1:8000/'
uid = '03kw1cc'
cmm = 'test'

def commands():
    content = {'response': cmm, 'client': uid, 'time_received': '',
               'exec_duration': '', 'directory': ''}
    sender = requests.post(f'{endpoint_1}command_feedback', json=content)
    print(sender)



commands()
