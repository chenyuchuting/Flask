from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    response = Response('设置cookie')
    response.set_cookie('username', 'chen')
    return response

@app.route('/del/')
def del_cookie():
    response = Response('删除cookie')
    response.delete_cookie('username')
    return response

if __name__ == '__main__':
    app.run()
