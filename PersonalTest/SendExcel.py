#!/usr/bin/python3# -*-
# coding: utf-8 -*-
# @Time : 2020/8/17 9:27 上午
# @Author : 覃
# @Email : 972354178@qq.com
# @File : SendExcel.py
# @Project : DjangoProject
# @Describe : python 调用 环保税接口 导入Excel文件
import os

from PersonalTest import PostUtil


def organizeParam(url, param):
    reStr = PostUtil.postJSON(url, param)
    return reStr


def sendExcelToHbs(excelpath, url, jsondata):
    """
    excelpath: Excel 的存放路径 由 RPA 机器人传入
    url: 环保税 导入 Excel 接口地址 由 RPA 机器人传入
    jsondata: 组织 请求参数
    """
    with os.scandir(excelpath) as entries:
        for entry in entries:
            if entry.is_file():
                with open(entry.path, "rb") as f:
                    file = {f.name: f}
                    reStr = PostUtil.postFile(url, jsondata, file)
                    print(reStr)


excelpath = '/Users/qinyixiong/Desktop/3yue/3月盈科'
importExcelUrl = 'http://localhost:8080/HBS_SWGL/jf/taxCheck/importExcel'
getParamUrl = ''
userinfo = ''

jsdata = {"F_DJBH": "hehed朋哥123",  # 单据编号
          "F_DATE": "202006",  # 202006
          "F_KEY": "",  # 配置表 主表中对应的key
          "F_TYPE": "1",  # 导入类型 1 为 Excel导入
          "F_WRWLB": ""  # 污染物类别
          }

# jsonStr = json.dumps(jsdata, ensure_ascii=False).encode("utf-8").decode("latin-1")

