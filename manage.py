
from flask_script import Manager
from info import create_app, db
from flask_migrate import Migrate, MigrateCommand
import logging

'''
    项目启动文件
'''

app = create_app("development")
manage = Manager(app)
Migrate(app, db)
manage.add_command("db", MigrateCommand)



if __name__ == '__main__':
    # logging.debug("debug的日志信息")
    # logging.info("info的日志信息")
    # logging.warning("warnning的日志信息")
    # logging.debug("debug的日志信息")
    manage.run()
