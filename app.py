from flask import Flask
import yaml

app = Flask(__name__)
# 加载配置文件
with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    for key, value in data.items():
        app.config[key] = value

# 引入蓝图，api版本由各蓝图决定
from applications.api import api

app.register_blueprint(api)