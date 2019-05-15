#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint, request

api = Blueprint('api', __name__)

@api.route('/column',methods=['POST'])
def column():
    from applications.multiColumn import multiColumn
    return multiColumn(request).result()