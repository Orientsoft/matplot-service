# /usr/bin/python
# -*- coding:utf-8 -*-
import time
from io import BytesIO
import numpy as np
import matplotlib as mpl
from matplotlib.font_manager import *
from matplotlib import pyplot as plt
import logging
myfont = FontProperties(fname='/usr/share/fonts/msyh.ttf')
mpl.rcParams['axes.unicode_minus'] = False


def autolabel(rects, ax, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


class multiColumn:
    def __init__(self, request):
        self.request = request

    def result(self):
        coordinate = self.request.json.get('coordinate')
        data = self.request.json.get('data')
        logging.error(self.request.json)
        return self.draw(coordinate, data)

    @staticmethod
    def draw(coordinate, data):
        '''
        :param coordinate: {'x':[],'y':'金额'}
        :param data = [
                    {'value':[300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3],'label':'平均值'},
                    {'value':[30.2, 53.3, 75.9, 5862.5, 979.6, 1289.7, 1958.3],'label':'最大值'}
                ]
        :return:文件流
        '''
        try:
            # 柱状图的个数
            n = len(data)
            total_width = 0.8
            ind = np.arange(len(coordinate['x']))
            width = total_width / n
            fig, ax = plt.subplots()
            # y轴
            ax.set_ylabel(coordinate['y'],fontproperties=myfont)
            # x轴
            ax.set_xticks(ind)
            ax.set_xticklabels(coordinate['x'],fontproperties=myfont)

            ind = ind - (total_width - width) / 2
            i = 0
            for x in data:
                temp = ax.bar(ind + i * width, x['value'], width, label=x['label'])
                i += 1
                autolabel(temp, ax)

            ax.legend(prop=myfont)
            # 文件流
            canvas = fig.canvas
            buffer = BytesIO()
            canvas.print_png(buffer)
            stream = buffer.getvalue()
            buffer.close()
            return stream
        except Exception as e:
            return '参数错误，图片生成失败', 400
