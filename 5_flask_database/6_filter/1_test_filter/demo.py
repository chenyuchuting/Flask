from sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text, String, func, and_, or_
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

# 1 equal
# result = session.query(Article).filter(Article.id == 1).all()
# result = session.query(Article).filter_by(id = 1).all()  # 此方法不建议使用

# 2 not equal
# result = session.query(Article).filter(Article.id != 1).all()

# 3 like，ilike不区分大小写
# result = session.query(Article).filter(Article.title.like('title%')).all()

# 4 in和not in
# result = session.query(Article).filter(Article.id.in_([1, 2])).all()
# result = session.query(Article).filter(~Article.id.in_([1, 2])).all()
# result = session.query(Article).filter(Article.id.notin_([1, 2])).all()

# 5 is None
# result = session.query(Article).filter(Article.id == None).all()
# result = session.query(Article).filter(Article.id != None).all()

# 6 and和or，也可以从sqlalchemy导入and_或者or_
# result = session.query(Article).filter(Article.title == "abc", Article.price == 60).all()
result = session.query(Article).filter(or_(Article.title == "abcd", Article.price == 60)).all()
print(result)