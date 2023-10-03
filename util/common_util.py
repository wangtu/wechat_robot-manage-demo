"""
coding:utf-8
file: common_util.py
@desc:
"""
import datetime
import uuid

import yaml
from PyQt5.QtWidgets import QMessageBox


def read_yaml(path):
    with open(path, encoding='utf-8') as f:
        stm = f.read()
    content = yaml.load(stm, Loader=yaml.FullLoader)
    return content


def get_uuid():
    return str(uuid.uuid1()).replace('-', '')


def msg_box(widget, title, msg):
    QMessageBox.warning(widget, title, msg, QMessageBox.Yes)


def accept_box(widget, title, msg):
    return QMessageBox.warning(widget, title, msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)


def get_current_time():
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return dt


def get_return_day(day):
    return (datetime.datetime.now() + datetime.timedelta(days=day)).strftime('%Y-%m-%d %H:%M:%S')
