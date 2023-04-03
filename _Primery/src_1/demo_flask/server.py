from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return "Добрый день! Это ответ сервера!"

@app.route('/test/<fio>')
def demo(fio):
    return '''
        <html>
            <head>
                <title>Привет, {}</title>
            </head>
            <body>
                <h1>Добрый день, {}</h1>
            </body>
        </html>'''.format(fio,fio)

# Если просто открывается страница, то всегда запускается запрос GET
# Любые запросы по ссылке всегда обрабатываются методом GET
@app.route('/form',methods=['POST','GET'])
def form():
    if request.method == 'GET':
        print(request.args.get('age')) #так обрабатываем данные, поступающие по ссылке
        return '''
            <!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Пример обработки формы</title>
                    </head>
                    <body>
                        <h1>Демонстрация работы с формой</h1>
                        <form method="post">
                            <p>Введите ваше имя</p>
                            <input type="text" name="fio">
                            <p>Введите ваш Email</p>
                            <input type="text" name="email"><br><br>
                            <input type="submit" value="Отправить">
                        </form><hr>
                        <a href="?age=25">Перейти по ссылке</a>
                    </body>
                </html>'''
        # else:
        #     return "Ваш возраст: test"
    elif request.method == 'POST':
        return f"Имя: {request.form['fio']}<br>Email: {request.form['email']}"
    return "Ошибка!"

if __name__ == '__main__':
    app.run(port=8080,host='127.0.0.1')

