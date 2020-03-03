from sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
USERNAME = 'root'
PASSWORD = '123'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'.\
    format(username=USERNAME,
        password=PASSWORD,
        host=HOSTNAME,
        port=PORT,
        db=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
# Session的主要目的是建立与数据库的会话，它维护你加载和关联的所有数据库对象。
# sessionmaker方法创建了一个Session工厂
session = sessionmaker(engine)()


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# import random
# for i in range(1, 7):
#     article = Article(title="title%s" % i, price=random.randint(15, 100))
#     session.add(article)
#
# session.commit()

# 查询的是模型对象
# articles = session.query(Article).all()
# print(articles)

# 查询模型对象的属性
# articles = session.query(Article.title, Article.price).all()
# print(articles)

# 聚合函数的查询，首先要导入func
# articles = session.query(func.count(Article.id)).all()
articles = session.query(func.avg(Article.price)).all()
print(articles)