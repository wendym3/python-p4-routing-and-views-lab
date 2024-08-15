from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'<h1>{param}</h1>'

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(num) for num in range(param))
    return f'<pre>{numbers}\n</pre>'  

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return "Invalid operation", 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)
