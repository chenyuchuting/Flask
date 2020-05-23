# flask中一般使用flask-sqlalchemy来操作数据库，使用起来比较简单，易于操作。
from flask_sqlalchemy import SQLAlchemy


# 操作数据库需要先创建一个db对象，通常写在exts.py文件里。
# https://www.jianshu.com/p/f7ba338016b8
db = SQLAlchemy()