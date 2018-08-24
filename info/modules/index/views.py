from . import index_bp
from flask import session, current_app, render_template
from info import redis_store, models


@index_bp.route('/')
def hello_world():
    redis_store.set("name", "laowang")
    current_app.logger.debug("记录日志")
    session["name"] = "gaoyan"
    return render_template("news/index.html")
