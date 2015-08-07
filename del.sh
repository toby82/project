#!/bin/bash
work_dir=/home/Output_HuaCloud_ISO
cd $work_dir && find ./ -mtime +7 -name "*" -exec rm -fr {} \; 

