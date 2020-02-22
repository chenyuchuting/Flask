# 主程序模块命名为app.py，你也可以命名为hello.py
# 从flask包中导入Flask类
from flask import Flask

# Flask类是Flask的核心类
# 它提供了很多与程序相关的属性和方法。
# Flask类构造方法的第一个参数是模块或包的名称。
# __name__其实是个变量，程序来说（app.py） ， 这个值为app。
# Flask在相应的文件夹里找到需要的资源。
app = Flask(__name__)


# @app.route()是一个装饰器。
# 注册路由的步骤：建立关联的过程就是注册路由。
# 传入URL规则作为参数，让URL与函数建立关联。
# 第一个参数是URL规则，使用字符串表示，你可以了解下URL的构造
# /对应的是根地址，例如：http://127.0.0.1:5000/index
# 访问上述地址时，会执行hello_world函数，然后返回字符串给浏览器
@app.route('/index')
def hello_world():
    return 'Hello World!'


# 此条件分支在本文件执行的时候，才会执行app.run()的方法
# app.run()启动后就是启动了这个网站
if __name__ == '__main__':
    # 函数启动后，类似执行的如下代码
    # while True:
    # listen()
    # input()
    # 也可以指定端口port=8000
    app.run()

# 测试代码
from flask import Flask

app = Flask(__name__)


# app.debug = True
# app.config.update(DEBUG=True)
# import config
# app.config.from_object(config)
# app.config.from_pyfile('config.py')
@app.route('/')
def hello_world():
    # print(1/0)
    return 'Hello World!'


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
