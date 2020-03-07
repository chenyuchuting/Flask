from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 1数据库链接
USERNAME = 'root'
PASSWORD = '123'
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'.\
    format(username=USERNAME,
        password=PASSWORD,
        host=HOSTNAME,
        port=PORT,
        db=DATABASE)

# 配置使用的数据库URL
# bug处理网址：https://blog.csdn.net/normang/article/details/81273182
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 2创建ORM模型，
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.username


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    user = db.relationship("User", backref="articles")


# 3将模型映射到数据库
# db.drop_all()
# db.create_all()

# 4使用session数据创建
# user = User(username="python")
# article = Article(title="The official home of the Python", uid=1)
# article.user = user
# db.session.add(article)
# db.session.commit()

# 5 数据查询
# user = db.session.query(User).all()
# user = User.query.all()
# user = User.query.order_by(User.id.desc()).all()
# print(user)

# 数据修改
# user = User.query.filter(User.username == 'java').first()
# user.username = "php"
# db.session.commit()

# 数据删除
user = User.query.filter(User.username == 'php').first()
db.session.delete(user)
db.session.commit()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()