# 使用models目的是为了将创建数据库模型的代码与主程序代码分离
# migrate的作用就是在数据库字段改变时不用drop表直接做更新操作
# Flask Script扩展提供向Flask插入外部脚本的功能
# 包括运行一个开发用的服务器，一个定制的Python shell，设置数据库的脚本

from flask_script import Manager
from app import app
from exts import db
from flask_migrate import Migrate, MigrateCommand
from models import User


manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()