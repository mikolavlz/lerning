import json

from flask import Flask,request,render_template
import pymysql

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    connect = pymysql.connect(host="localhost",
                              user="root",
                              password="root",
                              db="cars",
                              cursorclass=pymysql.cursors.DictCursor #для возможности получать данные в виде словаря
                              )

    with connect: #при успешном коннекте к базе
        cur = connect.cursor() #объект для возможности запускать sql запросы
        cur.execute('select * from marki')
        marks = cur.fetchall() #получаем информацию из базы в виде списка словарей

        if request.method == 'GET':
            return render_template("index_json.html",marks=marks)
        else: #Обрабатываем POST запрос
            id = request.form['id']#получили id марки
            if id != None:
                cur.execute(f"select * from models where id_mark={id}")
                models = cur.fetchall()
                answer = json.dumps(models)#преобразовали список словарей с данными в JSON
                return answer
            return "Error"
if __name__ == '__main__':
    app.run(port=8083,host='127.0.0.1')

