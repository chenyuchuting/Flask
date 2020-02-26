from flask import Blueprint, render_template

# name是为蓝本的名字，这个参数必须存在
# import_name是蓝本所在的包或模块
# 如果blue_static文件夹在chain文件下，则static_folder="chain/blue_static"
# 如果blue_static文件夹在user文件下，则static_folder="blue_static"
# users也是模板文件中的url_for('users.static', filename='admin_css.css')
user_bp = Blueprint('users', __name__,
                    url_prefix="/info",
                    template_folder="chain",
                    static_folder="blue_static",
                    )


@user_bp.route("/users_list/")
def user_info():
    # 返回的是user/chain/home.html文件
    return render_template('home.html')


@user_bp.route('/books/')
def book_list():
    return "图书列表"