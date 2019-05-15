# /usr/bin/python
# -*- coding:utf-8 -*-
import time
from io import BytesIO
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

mpl.rcParams[u'font.sans-serif'] = ['simhei']
mpl.rcParams['axes.unicode_minus'] = False

def multiLine(*args):
    '''
    :param args: 横坐标[],纵坐标[],....纵坐标n[]
    :return: https://url
    '''
    fig = plt.figure()
    plt.plot(*args)
    canvas = fig.canvas
    buffer = BytesIO()
    canvas.print_png(buffer)
    data = buffer.getvalue()
    buffer.close()
    return data