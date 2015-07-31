#/usr/bin/python
#coding=utf-8
__author__ = 'Administrator'
import re
teststr = "this is test ! # Halllllllllllll lsllsll"
nn = re.sub(r'#.*$',"",teststr)
print(nn)
