from sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text, String, func, and_, or_, ForeignKey
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
    username = Column(String(10), nullable=False)

    # extend = relationship("UserInfo", uselist=False)

    def __repr__(self):
        return self.username


class UserInfo(Base):
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(100), nullable=False)
    uid = Column(Integer, ForeignKey("user.id", ondelete="SET NULL"))

    author = relationship("User", backref=backref("extend", uselist=False))

    def __repr__(self):
        return self.id


Base.metadata.drop_all()
Base.metadata.create_all()

user = User(username="chain1")
info1 = UserInfo(address="123a", uid=1)
# info2 = UserInfo(address="456", uid=1)
# 通过User对象模型向UserInfo对象模型添加数据
# 一对一是没有append属性的
user.extend = info1
# user.extend.append(info2)

session.add(user)
session.commit()