#coding:utf-8
import urllib

import re

import time

"""
测试写入文件  换行
"""
timeMills = 2     #每两秒写入一行数据
page = urllib.urlopen('https://www.baidu.com/')
htmlcode = page.read()
print htmlcode
for i in range(30):
    htmlcode += 'url=https://www.baidu.com/" '
print htmlcode
reg = r'https://www.baidu.com/'#正则表达式
reg_img = re.compile(reg)#编译一下，运行更快
imglist = reg_img.findall(htmlcode)#进行匹配
print imglist

pageFile = open('pageCode.txt','w')#以写的方式打开pageCode.txt

for i in range(len(imglist)):
    print i
    if(i%4==0 and i!=0):
        pageFile.write("\n", )  # 写入
        time.sleep(timeMills)
        pageFile.flush()
    pageFile.write(imglist[i] + "     ")

pageFile.close()#开了记得关