# 首页模块

from flask import Blueprint

# 1. 创建蓝图对象

index_bp = Blueprint("index", __name__, url_prefix='/index')


from .views import *