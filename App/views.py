# views.py: 路由 + 视图函数

# 蓝图
from flask import Blueprint, render_template, request, redirect, session
from .models import *
from .myclass import *

blue = Blueprint('user', __name__)  # 创建名为user的蓝图对象


# 首页
@blue.route('/home/')
@blue.route('/')
def home():
    username = request.cookies.get('user')  # 从请求中获取名为‘user’的cookie值
    messages = []
    for title, essay in essays.items():
        messages.append({'title': title, 'introduce': essay.introduce})
    return render_template('home.html', username=username, messages=messages)
    # 渲染模板，将两个值传入作为模板参数
    # 第1个修改的地方


# 登录
@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':  # GET请求获取网页内容
        return render_template('login.html')  # 返回登录界面的模板
    if request.method == 'POST':  # POST请求提交表单信息
        username = request.form.get('username')  # 获取表单信息
        password = request.form.get('password')
        if user.log(username, password):  # 比对账号和密码
            re = redirect('/home/')  # 重定向到首页
            re.set_cookie('user', username)  # 设置cookie
            return re
        else:
            return render_template('login.html', err='error')  # 登录不成功


# 注册
@blue.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':  # 访问界面
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users.keys():  # 已被注册
            return render_template('register.html', info=True)
        else:  # 未被注册
            users[username] = user(username, password)
            re = redirect('/home/')
            re.set_cookie('user', username)
            return re


# 收藏
@blue.route('/collection/')
def collection():
    username = request.cookies.get('user')  # 从请求中获取名为user的cookie值，赋值给username
    messages = []
    for title in users[username].collection:
        introduce = essays[title].introduce
        messages.append({'title': title, 'introduce': introduce})
    return render_template('collection.html', username=username, messages=messages)


# 编辑
@blue.route('/edit/', methods=['GET', 'POST'])
def edit():
    username = request.cookies.get('user')
    if request.method == 'GET':
        return render_template('edit.html', username=username)
    if request.method == 'POST':
        title = request.form.get('title')
        introduce = request.form.get('introduce')
        text = request.form.get('content')  # 是跟html中的id进行联系
        temp = {'title': title, 'introduce': introduce, 'text': text, 'writer': username, 'review': []}
        essay(temp)
        return render_template('edit.html', username=username)


# 用户主页
@blue.route('/userhome/')
def userhome():
    username = request.cookies.get('user')
    messages = []
    print(users[username].essay)
    for title in users[username].essay:
        print(title)
        print(essays[title].introduce)
        messages.append({'title': title, 'introduce': essays[title].introduce})
    return render_template('userhome.html', username=username, messages=messages)


# 帖子
@blue.route('/postings/', methods=['GET', 'POST'])
def postings():
    username = request.cookies.get('user')
    title = request.args.get('title')
    if request.method == 'GET':
        message = {  # 创建的是字典
            'title': title,
            'introduce': essays[title].introduce,
            'text': essays[title].text,
            'writer': essays[title].writer,
            'review': essays[title].review,
            'star': essays[title].star,
            'col': False
        }
        if username and title in users[username].collection:
            message['col'] = True
        return render_template('postings.html', username=username, messages=message)
    if request.method == 'POST':
        if username:
            review = request.form.get('review')
            essays[title].review.append({'reader': username, 'speak': review})
            re = redirect(request.url)
            return re
        else:
            re = redirect('/login')
            return re


# 处理点赞
@blue.route('/starplus/')
def starplus():
    title = request.args.get('title')
    username = request.cookies.get('user')
    if username:
        essays[title].star += 1
        url = request.url.replace('starplus', 'postings')
        re = redirect(url)  # 重定向到当前界面
        return re
    re = redirect('/login')
    return re


# 点踩
@blue.route('/KeyboardMan/')
def KeyboardMan():
    title = request.args.get('title')
    username = request.cookies.get('user')
    if username:
        essays[title].star -= 1
        url = request.url.replace('KeyboardMan', 'postings')
        re = redirect(url)
        return re
    re = redirect('/login')
    return re


# 加入收藏夹
@blue.route('/collectionplus/')
def collectionplus():
    title = request.args.get('title')  # 获取标题
    username = request.cookies.get('user')
    if username:  # 用户是否登录
        users[username].collection.append(title)  # 添加入用户收藏夹
        url = request.url.replace('collectionplus', 'postings')
        re = redirect(url)
        return re
    re = redirect('/login')
    return re


# 取消收藏
@blue.route('/collectiondown/')
def collectiondown():
    title = request.args.get('title')
    username = request.cookies.get('user')
    users[username].collection.remove(title)
    url = request.url.replace('collectiondown', 'postings')
    re = redirect(url)
    return re


# 注销
@blue.route('/unlogin/')
def unlogin():
    response = redirect('/home/')
    response.delete_cookie('user')
    return response
