#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import urlparse

import config.forwardRequests as ForwardRequestsConfig
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
        data = urlBlacklistDel(data)
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
            line = line.replace("\r\n", '')
            line = line.replace("\n", '')
            line = line.replace("\r", '')
            black_url_list.append(line)
        f.close()

    return black_url_list

# url黑名单参数删除
def urlBlacklistDel(url):
    parsed = urlparse.urlsplit(url)
    i = 0
    url_parsed_parameter = ''
    if parsed.query != '':
        for parsed_parameter_list in parsed.query.split('&'):
            if parsed_parameter_list.find('=') != -1:
                parameter_list = parsed_parameter_list.split('=', 1)
                if len(parameter_list[0]) != 0:
                    if parameter_list[0] not in ForwardRequestsConfig.BLACKLIST_PARAMETER_LIST:
                        i = i+1
                        if i == 1:
                            url_parsed_parameter = '?' + url_parsed_parameter + parameter_list[0] + '=' + parameter_list[1]
                        else:
                            url_parsed_parameter = url_parsed_parameter + '&' + parameter_list[0] + '=' + parameter_list[1]
    
    return parsed.scheme + '://' + parsed.netloc + parsed.path + url_parsed_parameter
    

    