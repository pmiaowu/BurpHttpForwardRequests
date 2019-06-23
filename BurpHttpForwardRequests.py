#!/usr/bin/python
# -*- coding: utf-8 -*-

from burp import IBurpExtender
from burp import IHttpListener

from application.tag import tag

import bootstrap.helpers as helpers
import sys

reload(sys)
sys.setdefaultencoding('utf8')

NAME = u'http请求转发插件'
VERSION = '1.0'

# 是否启动插件
IS_START = True

# 是否启动url重复验证
# True 开启验证, False 关闭验证
URL_REPEATED_VERIFY = True

class BurpExtender(IBurpExtender, IHttpListener):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()

        # 设置扩展名
        callbacks.setExtensionName(NAME)

        # 注册一个 HTTP 监听器
        callbacks.registerHttpListener(self)

        # 界面加载
        self.tags = tag(self._callbacks, NAME, IS_START, URL_REPEATED_VERIFY)
        self.tags.tagLoad()

        print(u'%s-加载成功' % (NAME))
        print(u'版本: %s' % (VERSION))
        print(u'作者: P喵呜-phpoop')
        print(u'QQ: 3303003493')
        print(u'GitHub: https://github.com/pmiaowu')
        print(u'Blog: https://www.yuque.com/pmiaowu')
        print(u'===================================')
        print('')

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        # 过滤 非响应的请求
        if messageIsRequest:
            return

        # 只处理Proxy模块的请求
        if toolFlag not in [4]:
            return

        if self.tags.isStartBox() == False:
            return

        # 获取请求包返回的服务信息
        host, port, protocol, is_https = self.getServerInfo(messageInfo.getHttpService())

        # 判断是否处于url黑名单之中
        if host in helpers.blackUrlList():
            return

        # 获取请求的信息
        request = messageInfo.getRequest()
        analyzedRequest, req_headers, req_method, req_parameters = self.getRequestInfo(request)

        req_url = self.getRequestUrl(protocol, port, req_headers)

        # 判断是否开启url重复验证
        if self.tags.urlRepeatedBox():
            # 判断是否重复url
            if helpers.isRepeatedUrl(host, req_url):
                return

        # 把请求发给扫描模块
        self._callbacks.doActiveScan(host, port, is_https, request) 

        print(u'请求转发成功 url: %s' % (req_url))
        print('')

    # 获取请求包返回的服务信息
    def getServerInfo(self, httpService):
        host = httpService.getHost()
        port = httpService.getPort()
        protocol = httpService.getProtocol()
        is_https = False
        if protocol == 'https':
            is_https = True

        return host, port, protocol, is_https

    # 获取请求的信息
    # 请求头,请求方法,请求参数
    def getRequestInfo(self, request):
        analyzedRequest = self._helpers.analyzeRequest(request)

        # 请求中包含的HTTP头信息
        req_headers = analyzedRequest.getHeaders()
        # 获取请求方法
        req_method = analyzedRequest.getMethod()  
        # 请求参数列表
        req_parameters = analyzedRequest.getParameters()

        return analyzedRequest, req_headers, req_method, req_parameters

    # 获取请求url
    def getRequestUrl(self, protocol, port, req_headers):
        link = req_headers[0].split(' ')[1]
        host = req_headers[1].split(' ')[1]
        return protocol + '://' + host + ':' + str(port) + link