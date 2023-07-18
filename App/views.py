
# views.py: 路由 + 视图函数

# 蓝图
from flask import Blueprint, render_template, request, redirect, session
from .models import *

blue = Blueprint('user', __name__)

# 首页
@blue.route('/home/')
@blue.route('/')
def home():
    username = request.cookies.get('user')
    return render_template('home.html', username=username)

@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'l' :
            re = redirect('/home/')
            re.set_cookie('user', username)
            return re
        else:
            return render_template('loginerr.html', username=username)


@blue.route('/unlogin/')
def unlogin():
    response = redirect('/home/')
    response.delete_cookie('user')
    return response