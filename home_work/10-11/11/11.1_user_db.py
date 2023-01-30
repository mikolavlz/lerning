import json

with open('user.json', 'w') as file:
        file.write('''
        {"user": [
    {
      "username": "max",
      "pass": "32456245"
    },
    {
      "username": "alex",
      "pass": "467456"
    },
    {
      "username": "ivan",
      "pass": "67456"
    },
    {
      "username": "petr",
      "pass": "34567"
    }

  ]
}
        ''')

in_username = input('Введите имя пользователя')
user_db = "user.json"
data = json.loads(open(user_db).read())
for userid in data['user']:
    if userid['username'] == in_username.lower() :
        input = (f"Ваш username {in_username.lower()} Ваш пароль {(userid['pass'])}")
        break
    else:
        input =('Пользователь не найден')
print(input)