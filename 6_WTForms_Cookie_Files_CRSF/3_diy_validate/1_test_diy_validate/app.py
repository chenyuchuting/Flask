from flask import Flask, request, render_template
from forms import LoginForm

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "success"
        else:
            print(form.errors)
            return 'fail'


if __name__ == '__main__':
    app.run()
