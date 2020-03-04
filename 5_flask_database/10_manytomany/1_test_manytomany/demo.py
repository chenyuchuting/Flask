from sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text, String, func, and_, or_, ForeignKey, Table
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

article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("article.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True),
)


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)

    def __repr__(self):
        return self.title


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    articles = relationship("Article", backref="tags", secondary=article_tag)

    def __repr__(self):
        return self.name


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# article1 = Article(title="article1")
# article2 = Article(title="article2")
#
# tag1 = Tag(name="tag1")
# tag2 = Tag(name="tag2")
#
# article1.tags.append(tag1)
# article1.tags.append(tag2)
#
# article2.tags.append(tag1)
# article2.tags.append(tag2)
#
# session.add(article1)
# session.add(article2)
#
# session.commit()

# article = session.query(Article).first()
# result = article.tags

tag = session.query(Tag).first()
result = tag.articles
print(result)