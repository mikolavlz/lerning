from flask import Flask,request,render_template

app = Flask(__name__)


# Пример отправки данных в представление

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/calc',methods=['POST'])
def calc():
    if request.method == 'POST':
        a = int(request.form['n1'])
        b = int(request.form['n2'])
        c = (request.form['znak'])
        s = a + b
        if c == "+":
            otv = a + b
        if c == "-":
            otv = a - b
        if c == "*":
            otv = a * b
        if c == "/":
            if b == 0:
                otv = "На ноль делить нельзя"
            else:
                otv = a / b
    return render_template("answer.html",a=a,b=b,c=c,otv=otv)

if __name__ == '__main__':
    app.run(port=8090,host='127.0.0.1')