from flask import Flask, render_template

# 在设置了template_folder参数后，这个程序要重新启动才会有效
# app = Flask(__name__, template_folder='D:/templates')
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index/')
def index():
    return render_template('index.html', username='链条')


@app.route('/blog/')
def blog():
    return render_template('blog/blog.html')


@app.route('/blog_para/')
def blog_para():
    context = {
        "name": "链条",
        "age": '12',
        'sex': 'man'
    }
    # return render_template('index.html', context=context)也正确，
    return render_template('index.html', **context)


@app.route('/login/')
def login():
    # 在HTML模板中加入未知的参数，例如
    # <a href="{{ url_for('login', name='Chain') }}">点击登录</a>
    # 返回的时URL:http://127.0.0.1:5000/login/?name=Chain
    return render_template('login.html')


if __name__ == '__main__':
    app.run()