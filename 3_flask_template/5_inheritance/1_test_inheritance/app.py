from flask import Flask, render_template

app = Flask(__name__)
# 配置自动加载模板文件
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
