import requests
import time
import json

start = time.time()
print('starting...')

content = {"message": "This is a test messagvvvve"}
print(type(content))

endpoint_1 = 'http://127.0.0.1:8000/'
endpoint_2 = 'https://xremote.herokuapp.com/'

test = requests.post(endpoint_1, json=content)

print(test.json())
print('finished in: ', time.time() - start)
