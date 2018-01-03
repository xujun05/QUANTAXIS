# -* coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) 2016-2017 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import getopt
import os
import sys
import threading
import time


def Usage():
    usage_str = '''''说明： 
    \t定时器 
    \timer.py -h 显示本帮助信息，也可以使用--help选项 
    \timer.py -d num 指定一个延时时间（以毫秒为单位） 
    \__t                    也可以使用--duration=num选项 
    '''
    print(usage_str)


def args_proc(argv):
    '''''处理命令行参数'''
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hd:', ['help', 'duration='])
    except getopt.GetoptError as err:
        print('错误！请为脚本指定正确的命令行参数。\n')
        Usage()
        sys.exit(255)

    if len(opts) < 1:
        print('使用提示：缺少必须的参数。')
        Usage()
        sys.exit(255)

    usr_argvs = {}
    for op, value in opts:
        if op in ('-h', '--help'):
            Usage()
            sys.exit(1)
        elif op in ('-d', '--duration'):
            if int(value) <= 0:
                print('错误！指定的参数值%s无效。\n' % (value))
                Usage()
                sys.exit(2)
            else:
                usr_argvs['-d'] = int(value)
        else:
            print('unhandled option')
            sys.exit(3)

    return usr_argvs


def timer_proc(interval_in_millisecond):
    loop_interval = 10      # 定时精度，也是循环间隔时间（毫秒），也是输出信息刷新间隔时间，它不能大于指定的最大延时时间，否则可能导致无任何输出
    __t = interval_in_millisecond / loop_interval
    while __t >= 0:
        min = (__t * loop_interval) / 1000 / 60
        sec = (__t * loop_interval) / 1000 % 60
        millisecond = (__t * loop_interval) % 1000
        print('\rThe remaining time:%02d:%02d:%03d...' %
              (min, sec, millisecond), end='\t\t')
        time.sleep(loop_interval / 1000)
        __t -= 1
    if millisecond != 0:
        millisecond = 0
        print('\rThe remaining time:%02d:%02d:%03d...' %
              (min, sec, millisecond), end='\t\t')
    print()


# 应用程序入口
if __name__ == '__main__':
    usr_argvs = {}
    usr_argvs = args_proc(sys.argv)
    for argv in usr_argvs:
        if argv in ('-d', '--duration'):
            timer_proc(usr_argvs[argv])
        else:
            continue
