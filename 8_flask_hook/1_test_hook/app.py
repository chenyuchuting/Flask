from flask import Flask, session, g, request
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello_world():
    # http://127.0.0.1:5000/?username=link
    username = request.args.get('username')
    g.username = username
    if hasattr(g, 'user'):
        print(g.user)
    return 'Hello World!'


@app.route("/list/")
def my_list():
    session['user_id'] = 1
    return "My list!"



# 只会在此项目首次访问的时候打印一次，再次访问则不打印
@app.before_first_request
def first_request():
    print("hello world!")


@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        g.user = 'chain'


if __name__ == '__main__':
    app.run()
