from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/ajax',methods=['POST'])
def calc():
    if request.method == 'POST':
        c = request.form["operation"]
        a = int(request.form['n1'])
        b = int(request.form['n2'])
        if c == "add":
            s = a + b
            return f"{a} + {b} = {s}"
        if c == "subtract":
            s = a - b
            return f"{a} - {b} = {s}"
        if c == "multiply":
            s = a * b
            return f"{a} * {b} = {s}"
        if c == "divide":
            s = a / b
            return f"{a} / {b} = {s}"
    return "Error"

if __name__ == '__main__':
    app.run(port=8081,host='127.0.0.1')

