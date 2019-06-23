#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

import os

# 判断是否重复url
def isRepeatedUrl(host, data):
    is_repeated = False

    i = datetime.datetime.now()
    file_name = u'./test_logs/ %s-%s-%s-%s.log' % (host, i.year, i.month, i.day)
    
    try:
        f = open(file_name, 'r')
    except IOError:
        add_file = open(file_name, 'w+')
        add_file.close()
        f = open(file_name, 'r')
    except:
        f.close()
    finally:
        if f.read().find(data) >= 0:
            is_repeated = True
        else:
            writeOutput(file_name, data)

        f.close()

    return is_repeated

# 数据写入
def writeOutput(address, data):
    f = open(address, 'a+')
    f.write(data + os.linesep)
    f.close()

# 黑名单列表
def blackUrlList():
    black_url_list = [] 

    dict_path = './black_url.txt'

    try:
        # 打开字典文件
        f = open(dict_path)
    except:
        f.close()
        return black_url_list
    finally:
        while True:
            line = f.readline()
            if not line:
                break
            black_url_list.append(line.replace("\n", ''))
        f.close()

    return black_url_list

    
    

    