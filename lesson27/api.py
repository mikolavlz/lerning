from flask import Flask , request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

@app.route('/test',methods = ['GET', 'POST'])
def test():
    if request.method == 'GET':
        return {
            'ответ' : 'тестовый GET ответ'
            'метод' : requests.method
                }
        if request.method == 'POST':
        return {
            'ответ': 'тестовый POST ответ'
                     'data' : requests.json
                     'метод': requests.method
                }


if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")
