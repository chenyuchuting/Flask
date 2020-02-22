from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 在一个URL中有一个手机号码的变量，必须限制为手机号码的格式
class TelephoneConveter(BaseConverter):
    # 在自定义类中，需要重新写这个变量的正则表达式
    regex = r'1[3456789]\d{9}'


# 假设用户在访问/tags/a+b
class ListConveter(BaseConverter):
    # 这个方法返回的值，将会被传递到视图函数中作为参数
    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        # 这个方法的返回值，将会在调用url_for()函数时生成符合要求的URL形式
        return '+'.join(value)


# 添加系统转换器的字典中
app.url_map.converters['tel'] = TelephoneConveter
app.url_map.converters['list'] = ListConveter


@app.route('/')
def hello_world():
    # 访问：http://127.0.0.1:5000/
    print(url_for('tags', boards=["a", 'b', 'c']))  # 输出：/tags/a+b+c
    return "hello world"


@app.route('/telephone/<tel:my_tel>')
def my_tel(my_tel):
    # 访问：http://127.0.0.1:5000/telephone/13523456789
    return '您的手机号码是%s' % my_tel


@app.route('/tags/<list:boards>')
def tags(boards):
    # 访问：http://127.0.0.1:5000/tags/a+b+c
    # 输出：你提交的板块是['a', 'b', 'c']
    return "你提交的板块是%s" % boards


if __name__ == '__main__':
    app.run()
