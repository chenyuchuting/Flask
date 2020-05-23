from flask_script import Manager
from app import app
from flask_migrate import MigrateCommand, Migrate
from exts import db
import models  # 一定要导入对象模型


manager = Manager(app)
# 用来绑定app和db到flask migrate的
Migrate(app, db)
manager.add_command('db', MigrateCommand)
# pycharm中打开Terminal
# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade


if __name__ == "__main__":
    manager.run()