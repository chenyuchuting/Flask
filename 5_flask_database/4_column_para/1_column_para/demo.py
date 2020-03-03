from sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum  # python3中独有的模块
from datetime import date, time, datetime

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
    # read_count = Column(Integer, default=0)
    create_time = Column(DateTime, default=datetime.now)
    title = Column(String(10), name="My_title",  nullable=False)  # 关键字参数需要放在后买你
    # code = Column(String(11), unique=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)


Base.metadata.drop_all()
Base.metadata.create_all()

# article = Article(title="abc")
# article = Article(title="abc")

# article1 = Article(code="15512341234")
# article2 = Article(code="15512341235")
# session.add_all([article1, article2])

article = Article(title="abc")
# article = session.query(Article).first()
# article.title = "123"
# session.commit()

session.add(article)
session.commit()