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
VERSION = '1.0.3'

MODULE = {4: 'proxy', 64: 'repeater'}

class BurpExtender(IBurpExtender, IHttpListener):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()

        # 设置扩展名
        callbacks.setExtensionName(NAME)

        # 注册一个 HTTP 监听器
        callbacks.registerHttpListener(self)

        # 界面加载
        self.tags = tag(self._callbacks, NAME)
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

        if self.tags.isStartBox() == False:
            return

        # 只处理白名单模块的请求
        if toolFlag not in self.tags.getWhiteListModule():
            return

        # 获取请求包返回的服务信息
        host, port, protocol, is_https = self.getServerInfo(messageInfo.getHttpService())

        # 判断是否处于url黑名单之中
        for black_url in helpers.blackUrlList():
            if black_url == host:
                return
            elif black_url[0] == '*' and black_url[1] == '.':
                black_url = black_url.replace('*.', '')
                if host.find(black_url) >= 0:
                    return

        # 判断是否处于白名单模式
        if self.tags.getWhiteList():
            is_white_url = False
            for white_url in self.tags.getWhiteList():
                if white_url == host:
                    is_white_url = True
                    break
                elif white_url[0] == '*' and white_url[1] == '.':
                    white_url = white_url.replace('*.', '')
                    if host.find(white_url) >= 0:
                        is_white_url = True
                        break
            if is_white_url == False:
                return

        # 获取请求的信息
        request = messageInfo.getRequest()
        analyzedRequest, req_headers, req_method, req_parameters = self.getRequestInfo(request)

        # Url调试功能
        for parameters in req_parameters:
            if parameters.getName() == 'is_burp_debug' and parameters.getValue() == 'True':
                return

        req_url = self.getRequestUrl(protocol, port, req_headers)

        # 获取响应包的信息
        res_headers, res_status_code, res_stated_mime_type, res_bodys = self.getResponseInfo(messageInfo.getResponse())

        # 黑名单资源不转发-避免一些无用的url也进行扫描
        if res_stated_mime_type in ['CSS', 'JPEG', 'GIF', 'PNG', 'image', 'video', 'script', '']:
            return

        # 判断是否开启url重复验证
        if self.tags.urlRepeatedBox() and toolFlag != 64:
            # 判断是否重复url
            if helpers.isRepeatedUrl(host, req_url):
                return

        # 把请求发给扫描模块
        self._callbacks.doActiveScan(host, port, is_https, request) 
        
        print('')
        print('===================================')
        print(u'来至模块: %s' % (MODULE[toolFlag]))
        print(u'请求转发成功 url: %s' % (req_url))
        print('===================================')
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

    # 获取响应的信息
    # 响应头,响应内容,响应状态码
    def getResponseInfo(self, response):
        analyzedResponse = self._helpers.analyzeResponse(response)

        # 响应中包含的HTTP头信息
        res_headers = analyzedResponse.getHeaders()
        # 响应中包含的HTTP状态代码
        res_status_code = analyzedResponse.getStatusCode()
        # 响应中返回的数据返回类型
        res_stated_mime_type = analyzedResponse.getStatedMimeType()
        # 响应中返回的正文内容
        res_bodys = response[analyzedResponse.getBodyOffset():].tostring() 

        return res_headers, res_status_code, res_stated_mime_type, res_bodys

    # 获取请求url
    def getRequestUrl(self, protocol, port, req_headers):
        link = req_headers[0].split(' ')[1]
        host = req_headers[1].split(' ')[1]
        return protocol + '://' + host + ':' + str(port) + link