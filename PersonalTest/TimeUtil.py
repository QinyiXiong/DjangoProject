#!/usr/bin/python3# -*-
# coding: utf-8 -*-
# @Time : 2020/9/16 11:02 上午
# @Author : error:8
# @File : TimeUtil.py
# @Project : DjangoProject
# @Describe : 时间工具

import time
import datetime


def getCurrentQuarter():
    """
    获取当前季度
    :return: data
    """
    now = datetime.datetime.now()
    # 当前季度
    now_quarter = now.month / 3 if now.month % 3 == 0 else now.month / 3 + 1
    return now_quarter


def getCurrentTime(format):
    '''
    根据格式，获取当前时间 （eg:"%Y-%m-%d %H:%M:%S"）
    :param format:
    :return:
    '''
    now_time = time.strftime(format, time.localtime())
    return now_time


def getLastMonth(format):
    '''
    根据格式，获取上一月份
    :param format:
    :return:
    '''
    now = datetime.datetime.now()
    this_month_start = datetime.datetime(now.year, now.month, 1)
    last_month_end = this_month_start - datetime.timedelta(days=1)
    last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1)
    resultTime = last_month_start.strftime(format)
    return resultTime


def getLastYear(format):
    '''
    根据格式，获取上一年时间
    :param format:
    :return:
    '''
    now = datetime.datetime.now()
    this_year_start = datetime.datetime(now.year, 1, 1)
    last_year_end = this_year_start - datetime.timedelta(days=1)
    last_year_start = datetime.datetime(last_year_end.year, 1, 1)
    resultTime = last_year_start.strftime(format)
    return resultTime


F_DATE = getLastMonth("%Y%m")
print(F_DATE)

'''

    获取上一季度
    
'''
# 获取当前季度
currentQuarter = getCurrentQuarter()
tempstr = ""
if currentQuarter == 1:
     tempstr = getLastYear("%Y") + "04"
else:
    tempstr = getCurrentTime("%Y") + "0" + str(int(currentQuarter - 1))

F_DATE = tempstr
print(F_DATE)





