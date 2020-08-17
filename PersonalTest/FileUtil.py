#!/usr/bin/python3# -*-
# coding: utf-8 -*-
# @Time : 2020/8/17 3:16 下午
# @Author : error:8
# @File : FileUtil.py
# @Project : DjangoProject
# @Describe : python 文件操作
import os
import shutil


def moveFileToAssingPath(oripath, assignpath):
    """
        将 oripath 目录下的所有文件 移动 至 指定目录 assignpath 下
        :param oripath: 原始文件所在目录
        :param assignpath: 指定目录
        :return:
    """
    with os.scandir(oripath) as entries:
        for entry in entries:
            if entry.is_file():
                dst = shutil.move(entry.path, assignpath)
                print(dst)


oripath = '/Users/qinyixiong/Desktop/3yue/heheda'
assignpath = '/Users/qinyixiong/Desktop/3yue/3月盈科'

moveFileToAssingPath(oripath, assignpath)
