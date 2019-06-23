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

class tag(ITab):
    def __init__(self, callbacks, name, is_start, url_repeated_verify):
        self._callbacks = callbacks
        self.name = name
        self.is_start = is_start
        self.url_repeated_verify = url_repeated_verify

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
        self.blackSettings = JPanel(GridBagLayout())
        
        c = GridBagConstraints()

        # 界面选项卡加载
        self.tag_1(c)
        self.tag_2(c)

        # 添加选项卡
        self.tabs.addTab(u'基本配置', self.settings)
        
        self._callbacks.customizeUiComponent(self.tabs)
        self._callbacks.addSuiteTab(self)

    # 选项卡1-标签1-ui
    def tag_1(self, c):
        # 创建 检查框
        self.is_start_box = JCheckBox(u'是否启动插件', self.is_start)
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
        self.url_repeated_box = JCheckBox(u'是否启动url重复验证', self.url_repeated_verify)
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
