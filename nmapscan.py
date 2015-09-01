#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import nmap
scan = []
input_data = raw_input('Please input hosts and ports: ')
scan_row = input_data.split(" ")
if len(scan_row) !=2:
    print "Input errors,example \"192.168.1.0/24 80,443,22\""
    sys.exit(0)
hosts = scan_row[0]
ports = scan_row[1]
try:
    nm = nmap.PortScanner()
except:
    print('error: ',sys.exc_info()[0])
    sys.exit(0)
try:
    nm.scan(hosts=hosts,arguments=' -v -sS -p '+ports)
except Exception,e:
    print "Scan error:"+str(e)

for host in nm.all_hosts():
    print('-' * 35 )
    print('Host : %s' % (host))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('*' * 20 )
        print('Protocal : %s' % proto)
        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print('Port : %s\tstate : %s' % (port,nm[host][proto][port]['state']))
