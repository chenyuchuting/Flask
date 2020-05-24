from flask import Flask
import config
from exts import db
from articleviews import article_bp

from models import User, Article, Tag


app = Flask(__name__)
app.config.from_object(config)  # 加载配置文件
app.register_blueprint(article_bp)
# 写完数据库配置后需要和app绑定
db.init_app(app)
# api = Api(app)


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
