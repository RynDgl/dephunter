import requests
import json

headers = {
    'Host': 'pypi.org',
    'Accept': 'application/json',
}

response = requests.get('https://pypi.org/pypi/PyAutoGUI/json', headers=headers)

py_lib = json.loads(response.text)

print(py_lib['info']['home_page'])
#for item in py_lib['info']:
    #print(item)
