#!/usr/bin/python3# -*-
# coding: utf-8 -*-
# @Time : 2020/8/17 9:25 上午
# @Author : qinyixiong
# @Email : 972354178@qq.com
# @File : __init__.py.py
# @Project : DjangoProject
import json
import os

from PersonalTest import PostUtil

if __name__ == '__main__':
    datapath = '/Users/qinyixiong/Desktop/3yue/3月盈科'
    hbsurl = 'http://localhost:8080/HBS_SWGL/jf/taxCheck/importExcel'
    jsdata = {"F_DJBH": "hehed朋哥123",  # 单据编号
              "F_DATE": "202006",  # 202006
              "F_KEY": "",  # 配置表 主表中对应的key
              "F_TYPE": "1",  # 导入类型 1 为 Excel导入
              "F_WRWLB": ""  # 污染物类别
              }
    # jsonStr = json.dumps(jsdata, ensure_ascii=False).encode("utf-8").decode("latin-1")

    with os.scandir(datapath) as entries:
        for entry in entries:
            if entry.is_file():
                with open(entry.path, "rb") as f:
                    print(f.name)
                    file = {f.name: f}
                    hehe = PostUtil.postFile(hbsurl, jsdata, file)
                    print(hehe)
