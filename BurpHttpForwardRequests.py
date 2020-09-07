#!/usr/bin/python
# -*- coding: utf-8 -*-

from burp import IBurpExtender
from burp import IHttpListener

from application.tag import tag
from application.hackhttp import hackhttp

import bootstrap.helpers as helpers
import sys

reload(sys)
sys.setdefaultencoding('utf8')

NAME = u'http请求转发插件'
VERSION = '1.3.1'

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
        print(u'咸鱼作者: P喵呜-phpoop')
        print(u'二改作者: 钧钧')
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

        # 是否转发请求的判断
        if toolFlag not in self.tags.getWhiteListModule() and self.tags.xrayIsSelect() == False:
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
                elif len(white_url) > 2 and white_url[0] == '*' and white_url[1] == '.':
                    white_url = white_url.replace('*.', '')
                    if host.find(white_url) >= 0:
                        is_white_url = True
                        break
            if is_white_url == False:
                return

        # 获取请求的信息
        request = messageInfo.getRequest()
        analyzedRequest, req_headers, req_method, req_parameters = self.getRequestInfo(request)

        # 请求方法过滤
        # 只允许白名单的http请求通过
        if req_method not in self.tags.getWhiteListHttpMethod():
            return

        # Url调试功能
        for parameters in req_parameters:
            if parameters.getName() == 'is_burp_debug' and parameters.getValue() == 'True':
                return

        # 获取请求url
        req_url = str(self._helpers.analyzeRequest(messageInfo).getUrl())

        # 获取响应包的信息
        res_headers, res_status_code, res_stated_mime_type, res_bodys = self.getResponseInfo(messageInfo.getResponse())

        # 黑名单资源不转发-避免一些无用的url也进行扫描
        if res_stated_mime_type in ['CSS', 'JPEG', 'GIF', 'PNG', 'image', 'video', 'script']:
            return

        # 黑名单后缀不转发
        permitted_file_extensions = ['js', 'css', 'ico', 'jpg', 'jpeg',
                                     'gif', 'png', 'woff', 'woff2', 'eot',
                                     'svg', 'mp3', 'wmv', 'asf', 'asx',
                                     'rm', 'rmvb', 'mp4', '3gp', 'mov',
                                     'm4v', 'avi', 'dat', 'mkv', 'flv',
                                     'vob','ttf','swf']

        no_parameter_url = req_url.split('?')[0]
        url_extension = no_parameter_url.split('.')[-1]
        if url_extension in permitted_file_extensions:
            return

        # 判断是否开启url重复验证
        if self.tags.urlRepeatedBox() and toolFlag != 64:
            # 判断是否重复url
            if helpers.isRepeatedUrl(host, req_url):
                return

        # 将请求转发给xray
        if self.tags.xrayIsSelect() == True:
            # 这里有个线程池，或许可以把timeout调小一点，毕竟这里只是转发
            xray_address = self.tags.xrayAddress().split(":")
            proxy_str = (xray_address[0], int(xray_address[1]))
            hh = hackhttp()
            hh.http(url=req_url,raw=request,proxy=proxy_str)

            print('')
            print('===================================')
            print(u'请求转发xray成功 url: %s' % (req_url))
            print('===================================')
            print('')

        # 把请求发给主动扫描模块
        if toolFlag in self.tags.getWhiteListModule():
            self._callbacks.doActiveScan(host, port, is_https, request)

            print('')
            print('===================================')
            print(u'来至模块: %s' % (MODULE[toolFlag]))
            print(u'请求方法: %s' % (req_method))
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