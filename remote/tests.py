import requests
import time
import json

start = time.time()
print('starting...')

content = {"message": "This is a test message"}
print(type(content))

endpoint = 'http://127.0.0.1:8000/'

test = requests.post(endpoint, json=content)

print(test.json())
print('finished in: ', time.time() - start)
