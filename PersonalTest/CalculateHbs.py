#!/usr/bin/python3# -*-
# coding: utf-8 -*-
# @Time : 2020/8/18 9:21 上午
# @Author : error:8
# @File : CalculateHbs.py
# @Project : DjangoProject
# @Describe : 导入excel完成之后 调用 环保税计算接口
import datetime
import json

from PersonalTest import PostUtil


def getInfoFromHbs(url, param):
    """
    从 环保税 获取业务信息
    :param url: 环保税 业务接口地址
    :param param: 请求参数
    :return: data
    """
    reStr = PostUtil.postJSON(url, param)
    print(reStr)
    data = json.loads(reStr).get("data")
    return data


getParamUrl = 'http://localhost:8080/HBS_SWGL/jf/index/getCalInfoByNowMon'  # 环保税 获取待办信息 接口
nowtime = datetime.datetime.now().strftime('%Y%m')  # 获取 当前日期  eg: 202008
print(nowtime)

param = {
    "f_date": nowtime
}
infolist = getInfoFromHbs(getParamUrl, param)  # 调用 环保税 获取待办信息 接口
print(infolist)

calculateUrl = 'http://localhost:8080/HBS_SWGL/jf/taxCalculate/calculateAction'
# http://localhost:8080/HBS_SWGL/jf/taxCalculate/calculateAction?YEAR=2020&MONTH=7&F_USER=ahk&A=true
# 根据 获取的待办信息列表 循环调用 环保税计算接口
for el in infolist:
    calParam = {
        "YEAR": el.get("YEAR"),
        "MONTH": el.get("MONTH"),
        "F_USER": el.get("F_USER")
    }

    if el.get("A") == 'true':
        calParam["A"] = 'true'

    if el.get("W") == 'true':
        calParam["W"] = 'true'

    if el.get("S") == 'true':
        calParam["S"] = 'true'

    if el.get("N") == 'true':
        calParam["N"] = 'true'

    print(PostUtil.postJSON(calculateUrl, calParam))



