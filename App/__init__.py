
# __init__.py :初始化文件，创建Flask应用 自动执行

from flask import Flask
from .views import blue

def creat_app():
    app = Flask(__name__)

    app.register_blueprint(blueprint=blue)

    return app


