from sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text, String, func, and_, or_, ForeignKey, Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
import enum  # python3中独有的模块
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
    age = Column(Integer, nullable=False)
    gender = Column(Enum("male", 'female', 'secret'), default="male")

    def __repr__(self):
        return self.username


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    uid = Column(Integer, ForeignKey("user.id"))

    author = relationship("User", backref=backref('articles', lazy="dynamic"))

    def __repr__(self):
        return self.title


# 创建基础的数据
# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username="python", age=16, gender='male')
# user2 = User(username="java", age=16, gender='male')
# user3 = User(username="php", age=18, gender='female')
# user4 = User(username="C++", age=17, gender='female')
#
# article1 = Article(title="title1", uid=1)
# article2 = Article(title="title2", uid=2)
# article3 = Article(title="title3", uid=2)
# article4 = Article(title="title4", uid=3)
#
# article1.author = user1
# article2.author = user2
# article3.author = user2
# article4.author = user3
#
# session.add_all([article1, article2, article3, article4])
# # 子查询创建的数据
# session.add(user4)
# session.commit()

# 分组group_by
# query()，count()，group_by()中的参数均是对模型来讲的，因为这个是对字段的操作，而非数据库和实例
# result = session.query(User.gender, func.count(User.id)).group_by(User.gender).all()

# 顺序：query()查询结果后再聚合，聚合结果之后再利用having()进行筛选，
# having()中的参数一定要注意，一定要与聚合的字段保持相同。
# result = session.query(User.age, func.count(User.id)).group_by(User.age).having(User.age<18).all()
# print(result)


# 找到所有的用户，按照发表的文章进行排序
# result = session.query(User.username, func.count(Article.id)).join(Article).group_by(User.id).order_by(func.count(Article.id).desc()).all()
# print(result)

# 子查询一。查询同一个对象模型
# 第一次查询的结果做为第二次查询数据的来源
# user = session.query(User).filter(User.username == "python").first()
# users = session.query(User).filter(User.age == user.age, User.gender == user.gender).all()
# print(users)

# 子查询2
# temp = session.query(User.age.label("age"), User.gender.label("gender")).filter(User.username == 'python').subquery()
# result = session.query(User).filter(User.age == temp.c.age, User.gender == temp.c.gender).all()
# print(result)
# 如果你足够的细心，你会发现这段话上面所有的代码全部都是单独的py文件，而非flask框架。
