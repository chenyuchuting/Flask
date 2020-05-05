from flask import Flask
from blinker import Namespace

app = Flask(__name__)

# Namespace命名空间
# 1. 定义信号
signalspace = Namespace()
my_signal = signalspace.signal('link')  # link为信号的名称

# 2.监听信号
def signal(sender):
    print(sender)
    print("这是一个信号！")
my_signal.connect(signal)

# 3. 发送一个信号
my_signal.send()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
