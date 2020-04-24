from flask import Flask, request, session, url_for, current_app
from werkzeug.local import Local
from threading import local


# 只要绑定在local对象上的属性
# 每个线程都是隔离的
# local1 = Local()


app = Flask(__name__)

# 如果你需要在没有激活上下文的情况下使用这些变量， 可以手动激活上下文。
# 程序上下文对象使用app.app_context（） 获取.
# 第一种方法
# app_context = app.app_context()
# app_context.push()
# print(current_app.name)

# 第二种方法
# with app.app_context():
#     print(current_app.name)

@app.route('/')
def hello_world():
    # print(current_app.name)
    print(url_for('index'))
    return 'Hello World!'


@app.route('/index/')
def index():
    return "首页！"


# print(url_for('index'))  # 会报错
# 手动推入请求上下文
# 请求上下文可以通过test_request_context()方法临时创建
with app.test_request_context():
    # 手动推入一个请求上下文到请求上下文栈中
    # 如果当前应用上下文栈中没有应用上下文
    # 那么会首先推入一个应用上下文到栈中
    print(url_for('index'))

if __name__ == '__main__':
    app.run()
