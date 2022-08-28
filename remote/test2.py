import requests
import os
from datetime import datetime


endpoint_1 = 'http://172.20.10.6:8000/'
uid = '03kw1cc'
name = 'test'


def commands():
    content = {'name': name, 'uid': uid}
    sender = requests.post(f'{endpoint_1}login', json=content)
    print(sender)


commands()
