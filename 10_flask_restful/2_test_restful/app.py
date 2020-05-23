from flask import Flask
import config
from exts import db
from flask_restful import Api, Resource, fields, marshal_with

from models import User, Article, Tag


app = Flask(__name__)
app.config.from_object(config)  # 加载配置文件
# 写完数据库配置后需要和app绑定
db.init_app(app)
api = Api(app)


# class Article(object):
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
# article = Article(title='Python', content='Star link')
#
# class ArticleView(Resource):
#
#     resource_fields = {
#         'title': fields.String(default='Java'),
#         'content1': fields.String(attribute='content')  # content1才是返回的数据，content是对象的属性值
#     }
#
#     # restful规范中，要求定义好了返回的参数
#     # 即使这个参数没有值，也应该返回一个None回去。
#     @marshal_with(resource_fields)
#     def get(self):
#         # return {"title": article.title, 'content': article.content}
#         return article
#
# api.add_resource(ArticleView, '/article/', endpoint='article')


class ArticleView(Resource):
    resource_fields = {
        'article_title': fields.String(attribute='title'),
        'content': fields.String,
        'author': fields.Nested({
            'username': fields.String,
            'email': fields.String
        }),
        'tags': fields.List(fields.Nested({
            "id": fields.Integer,
            'name': fields.String
        })),
        'read_count': fields.Integer(default=80)
    }

    @marshal_with(resource_fields)
    # http://127.0.0.1:5000/article/1/
    def get(self, article_id):
        article = Article.query.get(article_id)
        return article

api.add_resource(ArticleView, '/article/<article_id>/', endpoint='article')


@app.route('/')
def hello_world():
    # user = User(username='link', email='123@qq.com')
    # article = Article(title='Python', content='python content')
    # article.author = user
    # tag1 = Tag(name='前端')
    # tag2 = Tag(name='Python')
    # article.tags.append(tag1)
    # article.tags.append(tag2)
    # db.session.add(article)
    # db.session.commit()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
