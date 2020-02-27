from sqlalchemy import create_engine


USERNAME = 'root'
PASSWORD = '123456'
HOSTNAME = '127.0.0.1'
PORT = '3306'
# 一定要在数据库中创建test数据模型
DATABASE = 'test'


# dialect+driver://username:passwordehost:port/database
# dialect是数据的实现，比如MySQL，pymysql是数据的驱动
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'.\
    format(username=USERNAME,
           password=PASSWORD,
           host=HOSTNAME,
           port=PORT,
           db=DATABASE)

engine = create_engine(DB_URI)

conn = engine.connect()
result = conn.execute('select * from class')  # 前提是数据库中有class这个表
print(result.fetchone())