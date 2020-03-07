from sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text, String, func, and_, or_, ForeignKey, Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import date, datetime
import time

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

    user = relationship("User", backref=backref('articles', lazy="dynamic"))

    def __repr__(self):
        return self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()

# 创建基础的数据
# user = User(username="chain1")
# for i in range(1, 101):
#     article = Article(title="title%s" % i)
#     user.articles.append(article)
# session.add(user)
# session.commit()

# 分页的技术
# 查询前10条数据
# articles = session.query(Article).limit(10).all()

# 偏移10条数据再进行查询
# articles = session.query(Article).order_by(Article.id.desc()).offset(10).limit(10).all()

# 切片的操作
# articles = session.query(Article).slice(0, 10).all()
# articles = session.query(Article)[0:10]
# print(articles)


# 懒加载的技术
# 在relationship对象中增加lazy="dynamic"参数后
# 通过主表查询从表中的数据返回的就是Query对象的数据
# lazy的值还有select等
user = session.query(User).first()
print(user.articles.filter(Article.id>90).all())