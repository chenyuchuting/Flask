from flask import Flask, request, render_template
from forms import LoginForm, SettingsForm

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


# https://wtforms.readthedocs.io/en/latest/fields.html#field-definitions
# WTForms文档的访问网址
@app.route('/settings/', methods=['GET', 'POST'])
def settings():
    if request.method == "GET":
        form = SettingsForm()
        return render_template('settings.html', form=form)
    else:
        form = SettingsForm(request.form)
        pass


if __name__ == '__main__':
    app.run()
