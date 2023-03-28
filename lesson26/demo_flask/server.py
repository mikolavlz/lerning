from flask import Flask,request

app = Flask(__name__)
@app.route('/')
def index():
    return "Добрый день это сервер"
@app.route('/test/<fio>')
def fio(fio):
    return '''
   <html>
<table style="border-collapse: collapse; width: 100%; height: 82px;" border="1">
<tbody>
<tr style="height: 46px;">
<td style="width: 100%; height: 46px;">
<p>Привет</p>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 100%; height: 18px;">{}</td>
</tr>
<tr style="height: 18px;">
<td style="width: 100%; height: 18px;">&nbsp;</td>
</tr>
</tbody>
</table>
</html>
'''.format(fio)
@app.route('/form',methods=['POST','GET'])
def form():
    if request.method == 'GET':
        return '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <h1>Демонстрауия  работы</h1>
                <form method="post">
                    <p>введите ваше имя</p>
                    <input type="text" name="fio">
                    <p>введите ваше email</p>
                    <input type="text" name="email"><br><br>
                    <input type="submit" value="отправить">
            
                </form>
            </body>
            </html>
            '''
    elif request. method == 'POST':
        # print(f"имя {request.form['fio']} email {request.form['email']}")
        return f'{request.form["fio"]},{request.form["email"]}'


if __name__ == '__main__':
    app.run(port=8080,host='127.0.0.1')
