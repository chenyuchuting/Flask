from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base


# 1数据库链接
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
Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    age = Column(Integer, default=0)

    def __repr__(self):
        return self.username


Base.metadata.create_all()
