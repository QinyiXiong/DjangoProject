#!/usr/bin/python3# -*-
# coding: utf-8 -*-
# @Time : 2020/8/17 9:27 上午
# @Author : error:8
# @File : SendExcel.py
# @Project : DjangoProject
# @Describe : python 调用 环保税接口 导入Excel文件
import datetime
import json
import os

from PersonalTest import PostUtil


def getInfoFromHbs(url, param):
    """
    从 环保税 获取业务信息
    :param url: 环保税 业务接口地址
    :param param: 请求参数
    :return: data
    """
    reStr = PostUtil.postJSON(url, param)
    data = json.loads(reStr).get("data")
    return data


def sendExcelToHbs(excelpath, url, jsondata):
    """
    将 excelpath 路径下
    :param excelpath: Excel 的存放路径 由 RPA 机器人传入
    :param url: 环保税 导入 Excel 接口地址 由 RPA 机器人传入
    :param jsondata: 组织 请求参数
    :return:
    """
    with os.scandir(excelpath) as entries:
        for entry in entries:
            if entry.is_file():
                with open(entry.path, "rb") as f:
                    file = {f.name: f}
                    reStr = PostUtil.postFile(url, jsondata, file)
                    print(reStr)


excelpath = '/Users/qinyixiong/Desktop/3yue/3月盈科'  # excel 存储路径
importExcelUrl = 'http://localhost:8080/HBS_SWGL/jf/taxCheck/importExcel'  # 环保税 导入excel 接口
getParamUrl = 'http://localhost:8080/HBS_SWGL/jf/index/getCalInfoByNowMon'  # 环保税 获取待办信息 接口
nowtime = datetime.datetime.now().strftime('%Y%m')  # 获取 当前日期  eg: 202008
print(nowtime)
# 调用
param = {
    "f_date": nowtime
}

infolist = getInfoFromHbs(getParamUrl, param)  # 调用 环保税 获取待办信息 接口
infodict = infolist[0]  # 获取第一个信息

jsdata = {"F_DJBH": infodict.get("F_DJBH"),  # 单据编号
          "F_DATE": infodict.get("YEAR") + infodict.get("MONTH"),  # 202007
          "F_KEY": "HNLH_ZDJC",  # 配置表 主表中对应的key (盈科为：HNLH_ZDJC；LIMS:HNLH_SFJC)
          "F_TYPE": "1",  # 导入类型 1 为 Excel导入
          "F_WRWLB": "A"  # 污染物类别 A 或 W
          }
print(jsdata)
# sendExcelToHbs(excelpath, importExcelUrl, jsdata)  # 调用 环保税 导入excel 接口

jsdata["F_WRWLB"] = "W"
print(jsdata)
# sendExcelToHbs(excelpath, importExcelUrl, jsdata)  # 调用 环保税 导入excel 接口
