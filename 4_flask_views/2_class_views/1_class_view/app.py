# app.py
from flask import Flask, render_template, views, url_for, jsonify

app = Flask(__name__)
# 配置自动加载模板文件
app.config['TEMPLATES_AUTO_RELOAD'] = True


class JsonView(views.View):
    def get_data(self):
        return "data"

    # 这个方法必须要实现，dispatch是指处理，这里主要是处理请求
    def dispatch_request(self):
        return jsonify(self.get_data())


class Index(JsonView):
    def get_data(self):
        return {'Navigation1': 'home', 'Navigation2': 'book'}


# 类表示实现多个处理方法的视图,
# 类调用as_view（）方法把其转换为视图函数
# 传入自定义的端点值（用来生成URL），最后将它赋给view_func参数。
app.add_url_rule('/index/', endpoint="get_index", view_func=Index.as_view("back"))


class AdsView(views.View):
    def __init__(self):
        # 如果子类继承父类不做初始化，那么会自动继承父类属性。
        # 如果子类继承父类做了初始化，且不调用super初始化父类构造函数，那么子类不会自动继承父类的属性。
        # 如果子类继承父类做了初始化，且调用了super初始化了父类的构造函数，那么子类也会继承父类的属性。
        super(AdsView, self).__init__()
        self.context = {
            "variable1": "value1",
            "variable2": "value2"
        }


class ChargeView(AdsView):
    def dispatch_request(self):
        return render_template("charge.html", **self.context)


class LoginView(AdsView):
    def dispatch_request(self):
        self.context.update({
            "variable3": "value3",
        })
        return render_template("login.html",  **self.context)


app.add_url_rule('/charge/', view_func=ChargeView.as_view("get_charge"))
app.add_url_rule('/login/', view_func=LoginView.as_view("get_login"))


@app.route('/')
def hello_world():
    # 输出：/index/
    print(url_for("get_index"))
    # 输出：/charge/，这个是不指定endpoint关键字参数的情况下的输出
    print(url_for('get_charge'))
    return "hello world"


if __name__ == '__main__':
    app.run()