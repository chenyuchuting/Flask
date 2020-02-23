from flask import Flask, request, url_for
# import uuid
# print(uuid.uuid4())

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


@app.route('/list/')
def show_list():
    return "文章列表"


# URL向视图函数传递“list_id”参数
# 必须保持URL和视图函数中的“list_id”保持一致
@app.route('/list/<list_id>')
def show_article(list_id):
    return "%s页文章" % list_id


# int转换器的使用方法
@app.route('/user/<int:user_id>')
def show_user(user_id):
    return '作者的id是%s' % user_id


# any转换器的使用方法
@app.route('/<any(blog, crm):url_path>/<demo>')
def show_root(url_path, demo):
    if url_path == "blog":
        return '博客id%s' % demo
    else:
        return 'crm的id%s' % demo


# 使用methods参数传入一个包含监听的HTTP方法的可迭代对象
# 使用methods参数传入一个包含监听的HTTP方法的可迭代对象
# Flask会自动返回一个405错误响应
@app.route('/root', methods=['GET', 'POST'])
def root():
    return "设置监听的参数"


# 通过问号的形式传递参数
# 利用request中的args属性获取参数的值
# 客户端的URL设置为http://127.0.0.1:5000/get/?name=alex
@app.route('/get/')
def get():
    arg = request.args.get('name')
    return '获取的name值为%s' % arg


# 返回的是/list/1?count=2
# url_for第一个参数是视图函数的名字，数据类型为字符串
# 后面的参数是传递给视图函数，如果传递的参数在视图函数中已经定义
# 那么这个参数就会被当成path的形式给视图函数


@app.route('/')
def hello_world():
    # 打印的是：/login?auth=%2F
    print(url_for('login', auth='/'))
    # 如果这个参数之前没有在视图函数中定义，page=1已经定义
    # 那么这个参数变成查询字符串的形式放到视图函数中
    return url_for('my_list', page=1, count=2)


@app.route('/list/<page>')
def my_list(page):
    return "这是第%s页" % page


@app.route('/login')
def login():
    return 'login'


if __name__ == '__main__':
    app.run()