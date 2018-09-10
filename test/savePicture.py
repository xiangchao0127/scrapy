#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
"""
下载图片
"""

import os

a = 10
b = 20
list = [1, 2, 3, 4, 5]

if a in list:
    print "1 - 变量 a 在给定的列表中 list 中"
else:
    print "1 - 变量 a 不在给定的列表中 list 中"
if not os.path.exists("F:\ImageSave1"):
    os.mkdir("F:\ImageSave1")
for i in range(10,20):
  urllib.urlretrieve("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1536578822279&di=316109db85e187f45bda05d398e05d72&imgtype=0&src=http%3A%2F%2Fimg.bitscn.com%2Fupimg%2Fallimg%2Fc170602%2F1496412VE3K0-131A.jpg",r"F:\ImageSave1\nihao%d.jpg" % i)