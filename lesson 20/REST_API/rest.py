import requests
import json


# responce = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
# print(responce.text)
# print(type(responce))

# responce = requests.get('https://reqres.in/api/users?page=2')
# responce_dict = json.loads(responce.text)
# print(responce_dict['data'][0]['email'])

user = {'name':'ivanov','job':'admin'}
responce = requests.post('https://reqres.in/api/users',params=user)
print(responce.text)