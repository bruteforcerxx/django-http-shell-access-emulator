import requests
from threading import Thread
import os

endpoint_1 = 'http://127.0.0.1:8000/'
endpoint_2 = 'https://xremote.herokuapp.com/'

message = requests.get(f'{endpoint_1}script')
print(message)
