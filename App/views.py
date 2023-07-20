# views.py: 路由 + 视图函数

# 蓝图
from flask import Blueprint, render_template, request, redirect, session
from .models import *
import json

users = dict()
essays = dict()


class user:
    def __init__(self, username, password):
        self.name = username
        self.password = password
        self.essay = []
        self.collection = []
        users[username] = self


    @staticmethod
    def log(username, password):
        if username in users.keys():
            if users[username].password == password:
                return True
        return False

    @staticmethod
    def finduser(username):
        for user in users.values():
            if user.name == username:
                return user
        return None


class essay:
    def __init__(self, es):
        self.title = es['title']
        self.text = es['text']
        self.writer = es['writer']
        self.review = es['review']
        self.star = 0
        essays[self.title] = {'title': es['title'], 'text': es['text'], 'writer': es['writer'], 'review': es['review'], 'star': 0}
        user.finduser(es['writer']).essay.append({'title': es['title'], 'text': es['text'], 'writer': es['writer'], 'review': es['review']})


blue = Blueprint('user', __name__)

# 首页
@blue.route('/home/')
@blue.route('/')
def home():
    username = request.cookies.get('user')
    print(type(essays.values()))
    print(essays.values())
    return render_template('home.html', username=username, messages=essays.values())


@blue.route('/collection/')
def collection():
    username = request.cookies.get('user')
    user_message = users[username].collection
    return render_template('collection.html', username=username, messages=user_message)


# 登录
@blue.route('/login/', methods=['GET', 'POST'])
def login():
    print(users)
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if user.log(username, password):
            re = redirect('/home/')
            re.set_cookie('user', username)
            return re
        else:
            return render_template('login.html', err='error')


# 注册
@blue.route('/register/', methods=['GET', 'POST'])
def register():
    print(users)
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print('注册成功')
        print(username)
        print(password)
        users[username] = user(username, password)
        re = redirect('/home/')
        re.set_cookie('user', username)
        return re

# 编辑
@blue.route('/edit/', methods=['GET', 'POST'])
def edit():
    username = request.cookies.get('user')
    if request.method == 'GET':
        return render_template('edit.html', username=username)
    else:
        title = request.form.get('title')
        text = request.form.get('text')
        temp = {'title': title, 'text': text, 'writer': username, 'review': []}
        essay(temp)
        return render_template('edit.html', username=username)


# 用户主页
@blue.route('/userhome/')
def userhome():
    username = request.cookies.get('user')
    self_essays = user.finduser(username).essay
    return render_template('userhome.html', username=username, messages=self_essays)


#帖子
@blue.route('/postings/', methods=['GET', 'POST'])
def postings():
    username = request.cookies.get('user')
    title = request.args.get('title')

    if request.method == 'GET':
        print(title)
        message = {
            'title': title,
            'text': essays[title]['text'],
            'writer': essays[title]['writer'],
            'review': essays[title]['review'],
            'star': essays[title]['star']
        }
        print(message)
        print(type(message['review']))
        return render_template('postings.html', username=username, messages=message)
    if request.method == 'POST':
        review = request.form.get('review')
        print(review)
        essays[title]['review'].append({'reader': username, 'speak': review})
        re = redirect(request.url)
        return re


@blue.route('/starplus/')
def starplus():
    title = request.args.get('title')
    print(request.url)
    print(title)
    print('star')
    essays[title]['star'] += 1
    url = request.url.replace('starplus', 'postings')
    re = redirect(url)
    return re

@blue.route('/collectionplus/')
def collectionplus():
    title = request.args.get('title')
    username = request.cookies.get('user')
    print(request.url)
    print(title)
    print('collection')
    users[username].collection.append(essays[title])
    print(users[username].collection)
    url = request.url.replace('collectionplus', 'postings')
    re = redirect(url)
    return re


# 注销
@blue.route('/unlogin/')
def unlogin():
    response = redirect('/home/')
    response.delete_cookie('user')
    return response