
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
    message = {
        'title': '标题',
        'text': '内容'
    }

    return render_template('home.html', username=username, message=message)

@blue.route('/collection/')
def collection():
    username = request.cookies.get('user')
    return render_template('collection.html', username=username)


# 登录
@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'l':
            re = redirect('/home/')
            re.set_cookie('user', username)
            return re
        else:
            return render_template('login.html', err='error')


# 注册
@blue.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        return "注册成功"
        pass

# 编辑
@blue.route('/edit/', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        username = request.cookies.get('user')
        return render_template('edit.html',username=username)
    else:
        text = request.form.get('usertext')
        print(text)
        pass

# 用户主页
@blue.route('/userhome/')
def userhome():
    username = request.cookies.get('user')
    return render_template('userhome.html', username=username)

# 注销
@blue.route('/unlogin/')
def unlogin():
    response = redirect('/home/')
    response.delete_cookie('user')
    return response