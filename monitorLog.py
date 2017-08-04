#!/usr/bin/python
# encoding=utf-8
# Filename: monitorLog.py
import os
import signal
import sys
import subprocess
import time

#日志文件一般是按天产生，则通过在程序中判断文件的产生日期与当前时间，更换监控的日志文件
#程序只是简单的示例一下，监控test1.log 10秒，转向监控test2.log
def monitorLog(logFile):
    print '监控的日志文件 是%s' % logFile
    # 程序运行10秒，监控另一个日志
    start_time = time.time()
    popen = subprocess.Popen('tail -f ' + logFile, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = popen.pid
    popen.poll()
    print('Popen.pid:' + str(pid))
    while True:
        line = popen.stdout.readline().strip()
        popen.wait(30)
        # 判断内容是否有Started关键字
        if 'Started' in line:
            print(line)
            popen.kill()
            print '杀死subprocess'
            return True
        # 当前时间
        thistime = time.time()
        if thistime - start_time > 10:
            # 终止子进程
            popen.kill()
            print '杀死subprocess'
            return False

if __name__ == '__main__':
    logFile1 = "/var/log/ejlerp/pms.log"
    os.popen("sh /home/appusr/dubbo/ " + sys.argv[1])
    time.sleep(1)
    print monitorLog(logFile1)