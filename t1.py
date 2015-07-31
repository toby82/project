#coding=utf-8
__author__ = 'Administrator'
import re
try:
    with open('/etc/hosts','r') as f:
        for line in f.readlines():
            m = re.match(r'(.*)cobbler(.*)',line,re.I)
            if m:
                print line.split()[0]
            else:
                continue
except:
    print 'io error'