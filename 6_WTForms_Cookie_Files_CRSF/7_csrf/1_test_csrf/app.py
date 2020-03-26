from flask import Flask, render_template, views, request
from forms import RegistForm

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


class RegistView(views.MethodView):
    def get(self):
        return render_template('regist.html')

    def post(self):
        form = RegistForm(request.form)
        if form.validate():
            return "注册成功"
        else:
            print(form.errors)
            return "注册失败"


app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))


if __name__ == '__main__':
    app.run()
