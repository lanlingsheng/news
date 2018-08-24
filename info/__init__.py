from flask import Flask, session
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from config import config_dict
import logging
from logging.handlers import RotatingFileHandler


db = SQLAlchemy()
redis_store = None   # type: StrictRedis


def create_log(config_name):
    logging.basicConfig(level=config_dict[config_name].LOG_LEVEL)
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=100)
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    create_log(config_name)
    app = Flask(__name__)
    configClass = config_dict[config_name]
    app.config.from_object(configClass)
    # 懒加载，延迟加载
    db.init_app(app)
    global redis_store
    redis_store = StrictRedis(host=configClass.REDIS_HOST, port=configClass.REDIS_PORT, db=configClass.REDIS_NUM)
    CSRFProtect(app)
    Session(app)
    # 导入蓝图（延迟导入：解决循环导入文件的问题）
    from info.modules.index import index_bp
    app.register_blueprint(index_bp)

    return app


