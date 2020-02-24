from flask import Flask, jsonify
from werkzeug.wrappers import Response
# flask=werkgeug+sqlalchemy+jinja2

app = Flask(__name__)


# 必须继承自Response类
# 必须实现类方法force_type()
class JsonResponse(Response):
    # 这个方法只有是视图函数返回非响应的字段才会使用，例如列表
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            # jsonify()将字典转换成json对象，还生成一个response对象
            response = jsonify(response)
        return super(JsonResponse, cls).force_type(response, environ)


# 必须指定app.
app.response_class = JsonResponse


@app.route('/')
def hello_world():
    # 等同于Response('hello', status=200, content_type='text/html')
    return 'Hello World!'


@app.route('/blog')
def blog():
    # 如果直接['a', 'b']，在浏览器访问该URL时会报错。
    return 'blog', 200, {'name': 'chain'}


@app.route('/articles')
def my_articles():
    return {'title': "new world", 'tag': 'python'}


if __name__ == '__main__':
    app.run()
