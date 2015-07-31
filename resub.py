#/usr/bin/python
#coding=utf-8
"""
this is test doc!
"""
__author__ = 'Administrator'
import re
with open('/etc/hosts','r') as f:
    for line in f.readlines():
        teststr = "this is test 中文！# Halllllllllllll lsllsll"
        nn = re.sub(r'cn.cn',"com",line)
        print(nn)
        #print(__doc__)