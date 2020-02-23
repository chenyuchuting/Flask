from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# GET和POST请求区分
@app.route('/login/')
def login():
    if request.method == 'GET':
        return "GET请求"
    else:
        return 'POST请求'


@app.route('/blog/')
def home():
    # http://127.0.0.1:5000/blog/?name=chain
    if request.args.get('name'):
        return '欢迎登录'
    else:
        return redirect(url_for('login'), code=302)


if __name__ == '__main__':
    # 首先在其它的电脑中使用ping命令访问本电脑是否能够链接
    # 其次在其它的电脑浏览器中输入本机ip:9000即可访问
    app.run(host='0.0.0.0', port=9000)