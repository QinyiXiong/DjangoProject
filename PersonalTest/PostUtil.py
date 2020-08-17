#!/usr/bin/python3# -*-
# coding: utf-8 -*-
# @Time : 2020/8/17 9:27 上午
# @Author : error:8
# @File : PostUtil.py
# @Project : DjangoProject
# @Describe : Post 请求工具
import requests


def setHeader(url, contentType):
    if url is None:
        return None

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': contentType,
        'Referer': url
    }

    return headers


def postFile(url, jsondata, file):
    # post 发送文件
    if url is None:
        return None

    r = requests.post(url, data=jsondata, files=file)

    return r.text


def postJSON(url, jsondata):
    # post请求 参数以json形式发送
    if url is None:
        return None

    r = requests.post(url, data=jsondata)

    return r.text
