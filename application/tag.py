#!/usr/bin/python
# -*- coding: utf-8 -*-

from burp import ITab

from java.awt import GridBagLayout
from java.awt import GridBagConstraints
from java.awt import Insets
from java.awt import Color
from java.awt import Font

from javax.swing import JLabel
from javax.swing import JPanel
from javax.swing import JCheckBox
from javax.swing import JTabbedPane

import config.forwardRequests as ForwardRequestsConfig

class tag(ITab):
    def __init__(self, callbacks, name):
        self._callbacks = callbacks
        self.name = name

    def getTabCaption(self):
        return self.name

    def getUiComponent(self):
        return self.tabs

    def setFontItalic(self, label):
        label.setFont(Font(label.getFont().getName(), Font.ITALIC, label.getFont().getSize()))

    def setFontBold(self, label):
        label.setFont(Font('Serif', Font.BOLD, label.getFont().getSize()))

    # 配置界面添加    
    def tagLoad(self):
        # 创建窗口 开始
        self.tabs = JTabbedPane()

        self.settings = JPanel(GridBagLayout())
        self.forward_requests_settings = JPanel(GridBagLayout())
        
        c = GridBagConstraints()

        # 界面选项卡1-标签加载
        self.tag_1(c)
        self.tag_2(c)

        # 界面选项卡2-标签加载
        self.tag_3(c)
        self.tag_4(c)

        # 添加选项卡
        self.tabs.addTab(u'基本配置', self.settings)
        self.tabs.addTab(u'http请求转发设置', self.forward_requests_settings)

        self._callbacks.customizeUiComponent(self.tabs)
        self._callbacks.addSuiteTab(self)

    # 选项卡1-标签1-ui
    def tag_1(self, c):
        # 创建 检查框
        self.is_start_box = JCheckBox(u'是否启动插件', ForwardRequestsConfig.IS_START)
        self.setFontBold(self.is_start_box)
        self.is_start_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 1
        self.settings.add(self.is_start_box, c)

        # 在窗口添加一句话
        is_start_box_lbl = JLabel(u'打勾-启动, 不打勾-关闭')
        self.setFontItalic(is_start_box_lbl)
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 2
        self.settings.add(is_start_box_lbl, c)

    # 选项卡1-标签1-值
    def isStartBox(self):
        return self.is_start_box.isSelected()

    # 选项卡1-标签2-ui
    def tag_2(self, c):
        # 创建 检查框
        self.url_repeated_box = JCheckBox(u'是否启动url重复验证', ForwardRequestsConfig.URL_REPEATED_VERIFY)
        self.setFontBold(self.url_repeated_box)
        self.url_repeated_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 3
        self.settings.add(self.url_repeated_box, c)

        # 在窗口添加一句话
        url_repeated_box_lbl = JLabel(u'打勾-开启验证, 不打勾-关闭验证')
        self.setFontItalic(url_repeated_box_lbl)
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 4
        self.settings.add(url_repeated_box_lbl, c)

    # 选项卡1-标签2-值
    def urlRepeatedBox(self):
        return self.url_repeated_box.isSelected()

    # 选项卡2-标签1-ui
    def tag_3(self, c):
        # 创建 检查框
        self.is_proxy_forward_requests_box = JCheckBox(u'是否启动Proxy模块请求转发(推荐打勾)', ForwardRequestsConfig.IS_START_PROXY_FORWARD_REQUESTS)
        self.setFontBold(self.is_proxy_forward_requests_box)
        self.is_proxy_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 1
        self.forward_requests_settings.add(self.is_proxy_forward_requests_box, c)

        # 在窗口添加一句话
        is_proxy_forward_requests_box_lbl = JLabel(u'打勾-启动, 不打勾-关闭')
        self.setFontItalic(is_proxy_forward_requests_box_lbl)
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 2
        self.forward_requests_settings.add(is_proxy_forward_requests_box_lbl, c)

    # 选项卡2-标签2-ui
    def tag_4(self, c):
        # 创建 检查框
        self.is_repeater_forward_requests_box = JCheckBox(u'是否启动Repeater模块请求转发', ForwardRequestsConfig.IS_START_REPEATER_FORWARD_REQUESTS)
        self.setFontBold(self.is_repeater_forward_requests_box)
        self.is_repeater_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 3
        self.forward_requests_settings.add(self.is_repeater_forward_requests_box, c)

        # 在窗口添加一句话
        is_repeater_forward_requests_box_lbl = JLabel(u'打勾-启动, 不打勾-关闭')
        self.setFontItalic(is_repeater_forward_requests_box_lbl)
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 4
        self.forward_requests_settings.add(is_repeater_forward_requests_box_lbl, c)
    
    # 获取允许转发的burp模块列表
    def getWhiteListModule(self):
        white_list_module = []

        if self.is_proxy_forward_requests_box.isSelected():
            white_list_module.append(4)
        if self.is_repeater_forward_requests_box.isSelected():
            white_list_module.append(64)

        return white_list_module

