from sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum  # python3中独有的模块
from datetime import date, time, datetime

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'  # 数据库中一定要先创建这个test数据库
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


class TagEnum(enum.Enum):
    python = 'python'
    flask = 'flask'


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # price = Column(Float)
    # is_delete = Column(Boolean)
    # 5代表所有数字的个数，2是小数点后的位数
    # price = Column(DECIMAL(5, 2))
    # tags = Column(Enum("python", "java"))
    # tags = Column(Enum(TagEnum))
    # create_date = Column(DATE)
    # create_datetime = Column(DateTime)
    # create_time = Column(Time)
    # create_text = Column(Text)
    longtext = Column(LONGTEXT)


Base.metadata.drop_all()
Base.metadata.create_all()
# article = Article(price=12.56)
# article = Article(is_delete=True)
# article = Article(price=198.24)
# article = Article(tags='python')
# article = Article(tags=TagEnum.flask)
# article = Article(create_date=date(2020, 1, 28))
# article = Article(create_datetime=datetime(2020, 1, 28, 11, 39, 49))
# article = Article(create_time=time(11, 39, 49))
# article = Article(create_text="1111")  # 输入中文的情况下报错，暂时不知道为什么出现错误
article = Article(longtext="123")
session.add(article)
session.commit()