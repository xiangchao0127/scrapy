#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
图片抓取
https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&fm=detail&lm=-1&st=-1&sf=2&fmq=1536570111785_R&fm=detail&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=d
"""
import urllib

import re

import os

import sys

url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&fm=detail&lm=-1&st=-1&sf=2&fmq=1536570111785_R&fm=det' \
      'ail&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=d'     #开始抓取的url
save_path = 'F:\ImageSave1\%d.jpg'   #保存图片的路径
page = urllib.urlopen(url)
htmlcode = page.read()
# print htmlcode
'''
https://(?!(\\.jpg|\\.png)).+?(\.jpg|\.png)
'''

reg = r'https://(?!(\\.jpg|\\.png)).+?(\.jpg|\.png)'#正则表达式
reg_img = re.compile(reg)#编译一下，运行更快
imglist = reg_img.finditer(htmlcode)#进行匹配
# print(len(imglist))
imglists = list(imglist)

news_ids = []
for id in imglists:
    if id.group() not in news_ids:
        news_ids.append(id.group())

if not os.path.exists(save_path):
    os.mkdir(save_path)
x = 0
for i in news_ids:
    urllib.urlretrieve(i,save_path % x)
    x+=1