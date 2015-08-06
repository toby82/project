#coding=utf-8
__author__ = 'Administrator'
import fileinput
for line in fileinput.input("/tmp/hosts",inplace=1):
    line = line.replace(".cn",".com")