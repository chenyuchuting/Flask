from flask import Flask, session, g, request, render_template, abort
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello_world():
    # http://127.0.0.1:5000/?username=link
    username = request.args.get('username')
    g.username = username
    if hasattr(g, 'user'):
        print(g.user)
    # return render_template('list.html', current_user='chain2')
    return render_template('index.html')


@app.route("/list/")
def my_list():
    session['user_id'] = 1
    user_id = request.args.get("user_id")
    # http://127.0.0.1:5000/list/?user_id=1
    if user_id == '1':
        return 'hello'
    else:
        abort(500)
    return render_template('list.html')



# 只会在此项目首次访问的时候打印一次，再次访问则不打印
@app.before_first_request
def first_request():
    print("hello world!")


@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        g.user = 'chain1'


@app.context_processor
def context_processor():
    # return {'current_user': 'chain2'}
    if hasattr(g, 'user'):
        return {'current_user': g.user}
    else:
        # return None  # TypeError:'NoneType'object is not iterable
        return {}


@app.errorhandler(500)
def server_error(error):  # error不可少
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
