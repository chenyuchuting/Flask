from flask_script import Manager

db_manager = Manager()

@db_manager.command
def init():
    print("迁移仓库创建完毕")

@db_manager.command
def revision():
    print("迁移脚本生成完成")

@db_manager.command
def upgrade():
    print("脚本映射数据库完成")