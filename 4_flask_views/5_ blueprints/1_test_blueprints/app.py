from flask import Flask, url_for
from user.admin import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)


@app.route('/')
def hello_world():
    print(url_for('users.user_info'))  # 输出：/info/users_list/
    return 'Hello World!'


if __name__ == '__main__':
    app.run()