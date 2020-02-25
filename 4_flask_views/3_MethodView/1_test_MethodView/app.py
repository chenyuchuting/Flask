from flask import Flask, views, render_template, request

app = Flask(__name__)
# 配置自动加载模板文件
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def hello_world():
    return "hello world"


class LoginView(views.MethodView):
    # __error
    def __error(self, error=None):
        # 必须以error=error传递error这个参数，因为前端模板有{{ error }}这个变量
        return render_template('login.html', error=error)

    def get(self):
        return self.__error()

    def post(self):
        # 必须对应前端的form表单的提交方式为：method="post"
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "link" and password == "123":
            return "登录成功"
        else:
            return self.__error(error="用户名或密码错误！")


# /login/必须加斜杠
# 否则会出现错误：ValueError: urls must start with a leading slash
app.add_url_rule('/login/', view_func=LoginView.as_view("login"))


if __name__ == '__main__':
    app.run()