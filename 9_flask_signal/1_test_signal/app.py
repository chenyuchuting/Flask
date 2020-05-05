from flask import Flask, request, g, template_rendered, render_template, got_request_exception
from blinker import Namespace
from signals import login_signal

app = Flask(__name__)

# # Namespace命名空间
# # 1. 定义信号
# signalspace = Namespace()
# my_signal = signalspace.signal('link')  # link为信号的名称
#
# # 2.监听信号
# def signal(sender):
#     print(sender)
#     print("这是一个信号！")
# my_signal.connect(signal)
#
# # 3. 发送一个信号
# my_signal.send()


# def template_rendered_func(sender, template, context):
#     print('sender', sender)
#     print('template', template)
#     print('context', context)
# template_rendered.connect(template_rendered_func)


def request_exception_log(sender, *args, **kwargs):
    print(sender)
    print(args)
    print(kwargs)
got_request_exception.connect(request_exception_log)


@app.route('/')
def hello_world():
    a = 1/0
    return render_template('index.html')

# 定义一个登录的信号，以后用户登录进来以后。
# 就发送一个登录信号，然后能够监听这个信号。
# 在监听到这个信号以后，就记录当前这个用户登录的信息。
# 用信号的方式，记录用户的登录信息。
@app.route('/login/')
def login():
    # http://127.0.0.1:5000/login/?username=chain
    username = request.args.get('username')
    g.username = username
    if username:
        # my_signal.send(username)
        # login_signal.send(username=username)
        login_signal.send()
        return "登录成功！"
    else:
        return "请输入用户名！"


if __name__ == '__main__':
    app.run()
