from flask import Blueprint, request, render_template, flash, redirect
from flask_login import login_user, logout_user, login_required, current_user

from apps.account.models import User
from apps.config import BLUEPRINT_ACCOUNT_KEY
from apps.ext import lm, db

account = Blueprint(BLUEPRINT_ACCOUNT_KEY, __name__, template_folder='templates')


# 插件必须要求实现的方法,session获取用户的对象
@lm.user_loader
def load_user(uid):
    return User.query.get(uid)


"""
login_user
login_out
login_required
current_user
"""
"""
一种直接通过输入/login/
另外一种 通过验证方法调转

"""


# 四个插件
@account.route('/login/', methods=['get', 'post'])
def login():
    current_user
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.values.get('username')
        password = request.values.get('password')
        users = User.query.filter(User.username == username)
        if users:
            if users.first() and users.first().is_active:
                user = users.first()
                if user.verify_password(password):
                    login_user(user, remember=True)
                    return redirect('/')
                else:
                    pass
                # 提示用户名或者密码错误
            else:
                pass
                # 表示用户未激活,请与管理员联系
                #          表示用户注册完成之后未激活用户
        else:
            pass
    #         用户名不存在
    return ''


@account.route('/register/')
def register():
    user = User(username='123456')
    user.password = '123'
    db.session.add(user)
    db.session.commit()
    return '注册成功'


@account.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect('/')


@account.route('/users/')
@login_required
def users():
    return '查看用户信息'
