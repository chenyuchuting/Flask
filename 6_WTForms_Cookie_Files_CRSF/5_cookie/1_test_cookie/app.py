from flask import Flask, request, Response
from datetime import datetime, timedelta
from crmviews import bp

app = Flask(__name__)
app.register_blueprint(bp)
# C:\Windows\System32\drivers\etc\hosts
# 在hosts文件中设置：127.0.0.1 chain.com
# 在hosts文件中设置：127.0.0.1 crm.chain.com
# 浏览器端访问：http://crm.chain.com:5000/
app.config['SERVER_NAME'] = 'chain.com:5000'


@app.route('/')
def hello_world():
    response = Response('设置cookie')

    # expires = datetime(year=2020, month=4, day=13, hour=16, minute=52, second=20)
    # response.set_cookie('username', 'chen', max_age=60)  # max_age是表示cookie有效的时间，以秒为单位
    # expires设置的是到期的时间，是格林尼治时间
    # response.set_cookie('username', 'chen',  expires=expires)

    expires = datetime.now() + timedelta(days=30, hours=16)
    response.set_cookie('username', 'chen', expires=expires, domain='.chain.com')
    return response

@app.route('/del/')
def del_cookie():
    response = Response('删除cookie')
    response.delete_cookie('username')
    return response

if __name__ == '__main__':
    app.run()
