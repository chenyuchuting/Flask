from flask import Flask, render_template, url_for


app = Flask(__name__)
# 配置自动加载模板文件
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def hello_world():
    # 输出的是/home/
    print(url_for("back"))
    return "hello world"


@app.route("/index/")
def get_index():
    return render_template('index.html')


def get_home():
    return render_template("home.html")


app.add_url_rule('/home/', endpoint="back", view_func=get_home)


if __name__ == '__main__':
    app.run()