from flask_script import Manager
from app import app, BackUser, db
from db_manage import db_manager

manager = Manager(app)
manager.add_command('db', db_manager)  # 关联，添加子命令


# manager.command使被装饰的函数变成命令
@manager.command
def hello():
    print('hello world')


# @manager.option('-u', '--username', dest='username')
# @manager.option('-a', '--age', dest='age')
# def add_user(username, age):
#     print("输入的用户名是：%s, 年龄是:%s" % (username, age))


@manager.option('-u', '--username', dest='username')
@manager.option('-e', '--email', dest='email')
def add_user(username, email):
    user = BackUser(username=username, email=email)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()