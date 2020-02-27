from flask import Flask, request, render_template
from wtforms import Form, StringField
from wtforms.validators import Length, EqualTo


class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message="用户名错误")])
    password = StringField(validators=[Length(min=3, max=10)])
    password_repeat = StringField(validators=[Length(min=3, max=10), EqualTo("password")])


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


if __name__ == '__main__':
    app.run()
