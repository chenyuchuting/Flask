rom sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text, String, func, and_, or_, ForeignKey, Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import date, datetime


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

engine = create_engine(DB_URI)
# declarative_base()是一个工厂函数，它为声明性类定义构造基类
Base = declarative_base(engine)
# Session的主要目的是建立与数据库的会话，它维护你加载和关联的所有数据库对象。
# sessionmaker方法创建了一个Session工厂
session = sessionmaker(engine)()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

    def __repr__(self):
        return self.username


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    uid = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", backref=backref('articles', order_by=create_time.desc()))

    # __mapper_args__ = {
    #     "order_by": create_time.desc()
    # }

    def __repr__(self):
        return self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='abc')
# article1 = Article(title="python", uid=1)
# article2 = Article(title="java", uid=1)
# session.add(user)
# session.add(article1)
# session.commit()
# time.sleep(2)
# session.add(article2)
# session.commit()

# 指定表中的某个字段排序
# articles = session.query(Article).order_by(Article.create_time).all()
# articles = session.query(Article).order_by(Article.create_time.desc()).all()
# articles = session.query(Article).order_by("create_time").all()
# print(articles)

# 在模型中定义代码排序
# articles = session.query(Article).all()
# print(articles)

# 在relationship对象中定义排序的方式
user = session.query(User).first()
result = user.articles
print(result)