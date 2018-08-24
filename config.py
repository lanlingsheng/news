from redis import StrictRedis
import logging

'''
    项目配置文件
'''

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:gaoyan987@127.0.0.1:3306/information_16"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_NUM = 6

    # SECRET_KEY = "SDFASDFASDFASDFASDFSFASFASDF"

    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_NUM)  # 使用 redis 的实例
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400
    SECRET_KEY = "W73UULUS4UFO5omviuVZz6+Bcjs5+2nRdvmyYNq1wEryZsMeluALSDGxGnuYoKX"


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    DEBUG = False


config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}