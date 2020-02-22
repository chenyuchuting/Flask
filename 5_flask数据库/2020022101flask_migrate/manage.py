from flask_script import Manager
from app import app
from exts import db
from flask_migrate import Migrate, MigrateCommand


manager = Manager(app)
# 用来绑定app和db到flask migrate的
Migrate(app, db)
# 添加Migrate的所有子命令到db下
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()