from flask import Flask, request, render_template
from forms import RegistForm, LoginForm
from uuid import uuid4

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/regist/", methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        form = RegistForm(request.form)
        if form.validate():
            return "注册成功"
        else:
            return form.errors


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "登录成功"
        else:
            return "登录失败"


print(uuid4())


if __name__ == '__main__':
    app.run()
