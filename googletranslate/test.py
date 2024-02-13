# -*- coding: utf-8 -*-

# Code Runner: Run in current directory


import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get('https://translate.google.com', verify=False)

with open('./test.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

# print(response.text)
print(response.status_code)