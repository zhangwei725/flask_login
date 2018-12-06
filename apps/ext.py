from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# 初始化第三方插件


def init_ext(app):
    init_db(app)
    init_login(app)


db = SQLAlchemy()
migrate = Migrate()


# 初始化数据库
def init_db(app):
    # 数据的连接的路径
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flask_login?charset=utf8'
    # 打印sql语句
    app.config['SQLALCHEMY_ECHO'] = True
    # 自动提交事务
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app=app, db=db)


# 实例化登录对象
lm = LoginManager()
"""
session
cookie

"""


# 什么

def init_login(app: Flask):
    lm.login_view = '/account/login/'
    # basic   strong  None
    lm.session_protection = 'strong'
    lm.init_app(app)


# 其他配置
"""
session 存储的位置
# cookie 相关配置
"""
