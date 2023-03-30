from flask import Flask,request, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template("form.html")
@app.route('/calc', methods = ['POST'])
def calc():
    if request.method == 'POST':
        a = int(request.form['n1'])
        b = int(request.form['n2'])
        s = a + b
        return render_template("answer.html",a=a,b=b,s=s)



if __name__ == '__main__':
    app.run(port=90,host='127.0.0.1')
