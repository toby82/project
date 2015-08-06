#coding=utf-8
__author__ = 'Administrator'
'''######################## '''
try:
    with open('/etc/hosts','r') as f:
        for line in f.readlines():
            #print type(line.split()[1])
            if line.split()[1] == 'cobbler.chinacloud.com.cn':
                print line.split()[0]
            else:
                continue
                #print 'None'
except:
    print 'io error'