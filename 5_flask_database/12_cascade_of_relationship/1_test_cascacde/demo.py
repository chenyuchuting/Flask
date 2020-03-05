from sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text, String, func, and_, or_, ForeignKey, Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
import enum  # python3中独有的模块
from datetime import date, time, datetime

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

    # articles = relationship("Article", cascade="save-update,delete")
    # comments = relationship("Comment")

    def __repr__(self):
        return self.name


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=True)
    uid = Column(Integer, ForeignKey("user.id"), nullable=False)

    # delete参数，从表中的数据删除，主表中的数据也会被删除，从表中的其它数据为NULL
    # cascade还有其它的参数delete-orphan，merge，expunge，all
    # cascade 表示级联操作，就是说如果主键表中被参考字段更新
    # 外键表中也更新，主键表中的记录被删除，外键表中改行也相应删除
    author = relationship("User",
                          backref=backref("articles",
                                          cascade="save-update,delete,delete-orphan, merge"
                                          ),
                          cascade="save-update,delete",
                          single_parent=True
                          )

    def __repr__(self):
        return self.title


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=True)
    uid = Column(Integer, ForeignKey("user.id"))

    author = relationship(User, backref="comments")

    def __repr__(self):
        return self.content


def init_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()

    user = User(name="chain1")
    article1 = Article(title="python", uid=1)
    article2 = Article(title="java", uid=1)
    # article1.author = user
    # article2.author = user

    comment1 = Comment(content="comment1", uid=1)

    session.add_all([user, article1, article2, comment1])
    session.commit()


def main():
    # article = session.query(Article).first()
    # session.delete(article)

    # user = session.query(User).first()
    # session.delete(user)

    user = session.query(User).first()
    comment2 = Comment(content="comment2", uid=1)
    user.comments.append(comment2)
    session.merge(user)
    session.commit()


if __name__ == "__main__":
    # init_db()
    main()