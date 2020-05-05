from blinker import Namespace
from datetime import datetime
from flask import request, g

# 1. 定义命名空间
namespace = Namespace()
login_signal = namespace.signal('login')

# 2. 监听
def login_log(sender):  # 可以通过g对象控制username
    now = datetime.now()
    ip = request.remote_addr
    log_line = '{username}*{now}*{ip}'.format(username=g.username, now=now, ip=ip)
    with open('login_log.txt', 'a') as fp:
        fp.write(log_line+'\n')

login_signal.connect(login_log)