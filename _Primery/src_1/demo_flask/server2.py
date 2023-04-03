from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

# Пример отправки данных в представление
@app.route('/demo')
def demo():
    fio = "Иван"
    return render_template('index2.html',fio=fio)

users = [
    {
        'name':'Вася',
        'age':25,
        'phone':'29347926'
    },
    {
        'name':'Петя',
        'age':27,
        'phone':'234353477'
    }
]

@app.route('/list')
def send_data():
    return render_template('list.html',users=users)



@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/calc',methods=['POST'])
def calc():
    if request.method == 'POST':
        a = int(request.form['n1'])
        b = int(request.form['n2'])
        s = a + b
    return render_template("answer.html",a=a,b=b,s=s)

if __name__ == '__main__':
    app.run(port=8090,host='127.0.0.1')