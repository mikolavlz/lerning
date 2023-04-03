from flask import Flask, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

@app.route('/test_api',methods=['GET','POST'])
def test():
    if request.method == 'GET':
        return {
            'ответ': 'Тестовый ответ сервиса на GET запрос',
            'метод': request.method
        }
    if request.method == 'POST':
        return {
            'ответ': 'Тестовый ответ сервиса на POST запрос',
            'data': request.json,
            'метод': request.method
        }

@app.route('/test_api/<int:item_id>',methods=['GET','PUT','DELETE'])
def demo(item_id):
    if request.method == 'GET':
        return {
            'id':item_id,
            'ответ': 'Тестовый ответ сервиса на GET запрос',
            'метод': request.method
        }
    if request.method == 'PUT':
        return {
            'id':item_id,
            'ответ': 'Тестовый ответ сервиса на PUT запрос',
            'метод': request.method,
            'body':request.json
        }


if __name__ == '__main__':
    app.run(port=8080,host='127.0.0.1')