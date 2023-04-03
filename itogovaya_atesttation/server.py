from flask import Flask, request, render_template

app = Flask(__name__)


def calc(sign):
    if sign == "sum":
        return lambda a, b: a + b
    if sign == "sub":
        return lambda a, b: a - b
    if sign == "mult":
        return lambda a, b: a * b
    if sign == "div":
        return lambda a, b: a / b if b != 0 else "Делить на 0 нельзя"
    return lambda a, b: "Неопознанный знак"


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/ajax', methods=['POST'])
def method():
    if request.method == 'POST':
        try:
            inp = request.form['calc']
            OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                         '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}
            def parse(line):
                num = ''
                for i in line:
                    if i in '1234567890.':
                        num += i
                    elif num:
                        yield float(num)
                        num = ''
                    if i in OPERATORS or i in '()':
                        yield i
                if num:
                    yield float(num)

            def sort(parsed):
                tmp = []
                for i in parsed:
                    if i in OPERATORS:
                        while tmp and tmp[-1] != '(' and OPERATORS[i][0] <= OPERATORS[tmp[-1]][0]:
                            yield tmp.pop()
                        tmp.append(i)
                    elif i == ')':
                        while tmp:
                            x = tmp.pop()
                            if x == '(':
                                break
                            yield x
                    elif i == '(':
                        tmp.append(i)
                    else:
                        yield i
                while tmp:
                    yield tmp.pop()

            def calc(sort):
                tmp = []
                for i in sort:
                    if i in OPERATORS:
                        y = tmp.pop()
                        x = tmp.pop()
                        tmp.append(OPERATORS[i][1](x, y))
                    else:
                        tmp.append(i)
                return tmp[0]

            a = (f'Ответ: { calc(sort(parse(inp)))}')

            return a
        except:
            return "ошибочка если не передается значение"
    return "не post запрос"


if __name__ == '__main__':
    app.run(port=8090, host='127.0.0.1')
