from sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text, String, func, and_, or_, ForeignKey, Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


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
    name = Column(String(50), nullable=True)

    def __repr__(self):
        return self.name


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=True)
    uid = Column(Integer, ForeignKey("user.id"), nullable=False)

    author = relationship("User", backref="articles")

    def __repr__(self):
        return self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(name="chain1")
# article = Article(title="python")

# 一对多数据添加
# 通过主表中relationship中articles列表形式添加
# user.articles.append(article)
# session.add(user)

# 如果通过从表添加，则直接可以通过属性赋值的方式添加
# article.author = user
# session.add(article)
# session.commit()

# 删除，在外键中添加nullable=False，再执行下述代码就会报错了
user = session.query(User).first()
session.delete(user)
session.commit()