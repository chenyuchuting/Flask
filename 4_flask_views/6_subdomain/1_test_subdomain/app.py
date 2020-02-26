from flask import Flask
from flask import Blueprint, render_template
from blue_prints.crm import crm_bp

app = Flask(__name__)
# 必须要加上端口号
app.config['SERVER_NAME'] = "chain.com:5000"
app.register_blueprint(crm_bp)


@app.route('/')  # 输入：chain.com
def hello_world():
    return 'Hello World!'


# 这个/是必须的，不能有其它的字符了
# http://crm.chain.com:5000/
@crm_bp.route("/")
def crm():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()