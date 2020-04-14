from flask_sqlalchemy import SQLAlchemy

# 把关系数据库的表结构映射到对象上
# ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。
db = SQLAlchemy()