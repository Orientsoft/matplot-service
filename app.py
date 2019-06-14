from flask import Flask
import yaml
import logging
import traceback

app = Flask(__name__)
# 加载配置文件
with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    for key, value in data.items():
        app.config[key] = value

# 引入蓝图，api版本由各蓝图决定
from applications.api import api

app.register_blueprint(api)


@app.errorhandler(Exception)
def error_handler(error):
    logging.error('Request Error: {}\nStack: {}\n'.format(error, traceback.format_exc()))
    return 'MATPLOT-SERVICE 未知错误', 500