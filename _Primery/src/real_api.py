from flask import Flask, request
from pip._internal import req

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
users = [
            {"id":1,"fio":"Вася","age":20},
            {"id":2,"fio":"Иван","age":27},
            {"id":3,"fio":"Роман","age":25}
]

@app.route('/list',methods=['GET'])

def test_get():
    if request.method == 'GET':
        return users

@app.route('/get_user/<int:user_id>',methods=['GET'])
def get_user_by_id(user_id):
    if request.method == 'GET':
        for user in users:
            if user["id"] == user_id:
                return user
    return "Error"

@app.route('/create',methods=['POST'])

def add_user():
    if request.method == 'POST':
        user = request.json #считали юзера из тела запроса, который отправил клиент
        users.append(user)
        return users
    return "error"

@app.route('/update/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    if request.method == 'PUT':
        for i,item in enumerate(users):
            if item["id"] == user_id:
                users.pop(i)
                new_user = request.json
                users.insert(i,new_user)
        return users
    return "error"

@app.route('/delete/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    if request.method == 'DELETE':
        for item in users:
            if item["id"] == user_id:
                users.remove(item)
        return users
    return "error"


if __name__ == '__main__':
    app.run(port=8081,host='127.0.0.1')