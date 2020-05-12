from flask import Flask, render_template, url_for
from flask_restful import Api, Resource, reqparse, inputs

app = Flask(__name__)
api = Api(app)


class LoginView(Resource):
    # postman:http://127.0.0.1:5000/login/link
    def post(self, username=None):
        parser = reqparse.RequestParser()
        # 需要在postman中输入key和value的值。
        # default值是username的默认值，如果客户端不传入username的值，则会使用default
        parser.add_argument('username', type=str, help='用户名错误！', default='abc', trim=False)
        parser.add_argument('password', type=str, help='用户名错误！')
        parser.add_argument('age', type=int, help='年龄错误')  # 输入：12a会出现错误
        parser.add_argument('gender', type=str,help='性别错误', choices=['male', 'female'])
        parser.add_argument('home_page', type=inputs.url, help='不是网址')
        parser.add_argument('telephone', type=inputs.regex(r'1[3578]\d{9}'),help='不是电话号码')
        parser.add_argument('birthday', type=inputs.date, help='不是日期')
        args = parser.parse_args()
        print(args)
        return {'username': username}


# 输入：http://127.0.0.1:5000/login/的方式是get请求。
# 要改变访问的方式，需要在https://www.postman.com/下载postman。
# http://127.0.0.1:5000/login/link
# http://127.0.0.1:5000/regist/
api.add_resource(LoginView, '/login/<username>','/regist/')


with app.test_request_context():
    # print(url_for('login'))  # api.add_resource(LoginView, '/login/', endpoint="login")
    # print(url_for('loginview'))  # api.add_resource(LoginView, '/login/')
    print(url_for('loginview', username='link'))  # api.add_resource(LoginView, '/login/<username>')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
