#!/usr/bin/env python
#coding=utf-8
__author__ = 'Administrator'
'''test  '''
import re
try:
    with open('/etc/hosts','r') as f:
        for line in f.readlines():
            m = re.search(r'cobbler',line,re.I)
            if m:
                print line.split()[0]
            else:
                continue
except:
    print 'io error'
