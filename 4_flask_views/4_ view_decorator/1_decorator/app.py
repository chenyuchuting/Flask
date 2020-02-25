from flask import Flask, request, views
from functools import wraps

app = Flask(__name__)
# 配置自动加载模板文件
app.config['TEMPLATES_AUTO_RELOAD'] = True


# 装饰器的作用:在不改变原有功能代码的基础上,添加额外的功能,如用户验证等
# @wraps(view_func)的作用:不改变使用装饰器原有函数的结构(如__name__, __doc__)
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = request.args.get("username")
        if username and username == 'chain':
            # *的变量名会存放所有未命名的变量参数,并且会把位置参数转换成元组的形式
            # 关键字参数**kwargs：把N个关键字参数，转换成了字典。
            return func(*args, **kwargs)
        else:
            return "请先登录"
    return wrapper


@app.route('/')
def hello_world():
    return "hello world"


@app.route('/setting/')
# login_required不用加括号，其次是要放在@app.route('/setting/')的下面
# 正常前端访问该url，界面显示请先登录，如果输入
# http://127.0.0.1:5000/setting/?username=chain，则会正常的显示设置页面
@login_required
def setting():
    return "设置页面"


class Information(views.View):
    decorators = [login_required]

    def dispatch_request(self):
        return "个人中心"


app.add_url_rule('/info/', view_func=Information.as_view("info"))


if __name__ == '__main__':
    app.run()
