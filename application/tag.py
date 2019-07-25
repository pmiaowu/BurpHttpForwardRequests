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

from javax.swing import JButton
from javax.swing import JTextArea
from javax.swing import JTextField
from javax.swing import JScrollPane
from javax.swing.text import Utilities
from javax.swing.text import DefaultHighlighter
from java.awt.event import MouseEvent
from java.awt.event import MouseAdapter

import os
import sys
import config.forwardRequests as ForwardRequestsConfig

reload(sys)
sys.setdefaultencoding('utf8')

white_list_names = [
]

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
        self.white_list_domain_settings = JPanel(GridBagLayout())
        self.white_list_http_method_settings = JPanel(GridBagLayout())

        c = GridBagConstraints()

        # 界面选项卡1-标签加载
        self.tag_1_1(c)
        self.tag_1_2(c)

        # 界面选项卡2-标签加载
        self.tag_2_1(c)
        self.tag_2_2(c)

        # 界面选项卡3-标签加载
        self.tag_3_1(c)

        # 界面选项卡4-标签加载
        self.tag_4_1(c)
        self.tag_4_2(c)
        self.tag_4_3(c)
        self.tag_4_4(c)
        self.tag_4_5(c)
        self.tag_4_6(c)
        self.tag_4_7(c)
        self.tag_4_8(c)
        self.tag_4_9(c)
        self.tag_4_10(c)
        self.tag_4_11(c)
        self.tag_4_12(c)
        self.tag_4_13(c)
        self.tag_4_14(c)
        self.tag_4_15(c)

        # 添加选项卡
        self.tabs.addTab(u'基本设置', self.settings)
        self.tabs.addTab(u'http请求转发设置', self.forward_requests_settings)
        self.tabs.addTab(u'白名单域名设置', self.white_list_domain_settings)
        self.tabs.addTab(u'白名单http方法设置', self.white_list_http_method_settings)

        self._callbacks.customizeUiComponent(self.tabs)
        self._callbacks.addSuiteTab(self)

    # 选项卡1-标签1-ui
    def tag_1_1(self, c):
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
    def tag_1_2(self, c):
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
    def tag_2_1(self, c):
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
    def tag_2_2(self, c):
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

    # 选项卡3-标签1-ui
    def tag_3_1(self, c):
        # 输入框-标题
        lblParams = JLabel(u'请填写域名:')
        self.setFontBold(lblParams)
        lblParams.setForeground(Color(0, 0, 153))
        c.gridx = 0
        c.gridy = 0
        c.insets = Insets(5, 5, 5, 5)
        c.fill = GridBagConstraints.NONE
        c.anchor = GridBagConstraints.FIRST_LINE_END
        self.white_list_domain_settings.add(lblParams, c)

        # 输入框
        self.white_list_text_field = JTextField()
        c.fill = GridBagConstraints.BOTH
        c.gridx = 1
        c.gridy = 0
        self.white_list_domain_settings.add(self.white_list_text_field, c)

        lblParamsNote = JLabel(u"白名单域名列表")
        self.setFontItalic(lblParamsNote)
        c.fill = GridBagConstraints.NONE
        c.gridx = 0
        c.gridy = 1
        self.white_list_domain_settings.add(lblParamsNote, c)

        # 添加 文本框
        self.white_list_text_area = JTextArea()
        self.white_list_text_area.setColumns(20)
        self.white_list_text_area.setRows(10)
        self.white_list_text_area.setEditable(False)
        c.fill = GridBagConstraints.BOTH
        self.white_list_mouse_listener = TextAreaMouseListener(self.white_list_text_area)
        self.white_list_text_area.addMouseListener(self.white_list_mouse_listener)

        # 向文本框添加数据
        for name in white_list_names:
            self.white_list_text_area.append(name + '\n' + os.linesep)
        c.gridx = 1
        c.gridy = 1
        sp = JScrollPane(self.white_list_text_area)
        self.white_list_domain_settings.add(sp, c)

        # 添加 删除 重置
        buttonsPanel = JPanel(GridBagLayout())
        _c = GridBagConstraints()
        _c.insets = Insets(3, 3, 3, 3)
        _c.gridx = 0
        _c.fill = GridBagConstraints.BOTH
        _c.weightx = 1
        _c.gridwidth = 1

        handlers = ButtonHandlers(self.white_list_text_field, self.white_list_text_area, self.white_list_mouse_listener, white_list_names)
        
        # 添加按钮
        self.white_list_add_button = JButton(u'添加', actionPerformed=handlers.handler_add)
        _c.gridy = 1
        buttonsPanel.add(self.white_list_add_button, _c)

        # 删除按钮
        self.white_list_rm_button = JButton(u'删除', actionPerformed=handlers.handler_rm)
        _c.gridy = 2
        buttonsPanel.add(self.white_list_rm_button, _c)

        # 重置按钮
        self.white_list_restore_button = JButton(u'重置', actionPerformed=handlers.handler_restore)
        _c.gridy = 3
        buttonsPanel.add(self.white_list_restore_button, _c)

        c.gridx = 2
        c.gridy = 1
        c.fill = GridBagConstraints.NONE
        self.white_list_domain_settings.add(buttonsPanel, c)

    # 获取白名单域名列表
    def getWhiteList(self):
        return self.text_area_to_list(self.white_list_text_area)
    
    # 获取指定text数据
    def text_area_to_list(self, text_area):
        l = []
        text_list = text_area.getText().strip().split('\n')
        for data in text_list:
            if data == '':
                continue
            data = data.replace("\n", '')
            data = data.replace("\r", '')
            data = data.strip(' ')
            l.append(data)
        return l

    # 选项卡4-标签1-ui
    def tag_4_1(self, c):
        # 创建 检查框
        self.is_get_forward_requests_box = JCheckBox(u'转发GET请求', ForwardRequestsConfig.IS_GET_FORWARD_REQUESTS)
        self.setFontBold(self.is_get_forward_requests_box)
        self.is_get_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 1
        self.white_list_http_method_settings.add(self.is_get_forward_requests_box, c)

    # 选项卡4-标签2-ui
    def tag_4_2(self, c):
        # 创建 检查框
        self.is_post_forward_requests_box = JCheckBox(u'转发POST请求', ForwardRequestsConfig.IS_POST_FORWARD_REQUESTS)
        self.setFontBold(self.is_post_forward_requests_box)
        self.is_post_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 2
        self.white_list_http_method_settings.add(self.is_post_forward_requests_box, c)

    # 选项卡4-标签3-ui
    def tag_4_3(self, c):
        # 创建 检查框
        self.is_put_forward_requests_box = JCheckBox(u'转发PUT请求', ForwardRequestsConfig.IS_PUT_FORWARD_REQUESTS)
        self.setFontBold(self.is_put_forward_requests_box)
        self.is_put_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 3
        self.white_list_http_method_settings.add(self.is_put_forward_requests_box, c)

    # 选项卡4-标签4-ui
    def tag_4_4(self, c):
        # 创建 检查框
        self.is_patch_forward_requests_box = JCheckBox(u'转发PATCH请求', ForwardRequestsConfig.IS_PATCH_FORWARD_REQUESTS)
        self.setFontBold(self.is_patch_forward_requests_box)
        self.is_patch_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 4
        self.white_list_http_method_settings.add(self.is_patch_forward_requests_box, c)

    # 选项卡4-标签5-ui
    def tag_4_5(self, c):
        # 创建 检查框
        self.is_delete_forward_requests_box = JCheckBox(u'转发DELETE请求', ForwardRequestsConfig.IS_DELETE_FORWARD_REQUESTS)
        self.setFontBold(self.is_delete_forward_requests_box)
        self.is_delete_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 5
        self.white_list_http_method_settings.add(self.is_delete_forward_requests_box, c)

    # 选项卡4-标签6-ui
    def tag_4_6(self, c):
        # 创建 检查框
        self.is_copy_forward_requests_box = JCheckBox(u'转发COPY请求', ForwardRequestsConfig.IS_COPY_FORWARD_REQUESTS)
        self.setFontBold(self.is_copy_forward_requests_box)
        self.is_copy_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 6
        self.white_list_http_method_settings.add(self.is_copy_forward_requests_box, c)

    # 选项卡4-标签7-ui
    def tag_4_7(self, c):
        # 创建 检查框
        self.is_head_forward_requests_box = JCheckBox(u'转发HEAD请求', ForwardRequestsConfig.IS_HEAD_FORWARD_REQUESTS)
        self.setFontBold(self.is_head_forward_requests_box)
        self.is_head_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 7
        self.white_list_http_method_settings.add(self.is_head_forward_requests_box, c)

    # 选项卡4-标签8-ui
    def tag_4_8(self, c):
        # 创建 检查框
        self.is_options_forward_requests_box = JCheckBox(u'转发OPTIONS请求', ForwardRequestsConfig.IS_OPTIONS_FORWARD_REQUESTS)
        self.setFontBold(self.is_options_forward_requests_box)
        self.is_options_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 8
        self.white_list_http_method_settings.add(self.is_options_forward_requests_box, c)

    # 选项卡4-标签9-ui
    def tag_4_9(self, c):
        # 创建 检查框
        self.is_link_forward_requests_box = JCheckBox(u'转发LINK请求', ForwardRequestsConfig.IS_LINK_FORWARD_REQUESTS)
        self.setFontBold(self.is_link_forward_requests_box)
        self.is_link_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 9
        self.white_list_http_method_settings.add(self.is_link_forward_requests_box, c)

    # 选项卡4-标签10-ui
    def tag_4_10(self, c):
        # 创建 检查框
        self.is_unlink_forward_requests_box = JCheckBox(u'转发UNLINK请求', ForwardRequestsConfig.IS_UNLINK_FORWARD_REQUESTS)
        self.setFontBold(self.is_unlink_forward_requests_box)
        self.is_unlink_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 10
        self.white_list_http_method_settings.add(self.is_unlink_forward_requests_box, c)

    # 选项卡4-标签11-ui
    def tag_4_11(self, c):
        # 创建 检查框
        self.is_purge_forward_requests_box = JCheckBox(u'转发PURGE请求', ForwardRequestsConfig.IS_PURGE_FORWARD_REQUESTS)
        self.setFontBold(self.is_purge_forward_requests_box)
        self.is_purge_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 11
        self.white_list_http_method_settings.add(self.is_purge_forward_requests_box, c)

    # 选项卡4-标签12-ui
    def tag_4_12(self, c):
        # 创建 检查框
        self.is_lock_forward_requests_box = JCheckBox(u'转发LOCK请求', ForwardRequestsConfig.IS_LOCK_FORWARD_REQUESTS)
        self.setFontBold(self.is_lock_forward_requests_box)
        self.is_lock_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 12
        self.white_list_http_method_settings.add(self.is_lock_forward_requests_box, c)

    # 选项卡4-标签13-ui
    def tag_4_13(self, c):
        # 创建 检查框
        self.is_unlock_forward_requests_box = JCheckBox(u'转发UNLOCK请求', ForwardRequestsConfig.IS_UNLOCK_FORWARD_REQUESTS)
        self.setFontBold(self.is_unlock_forward_requests_box)
        self.is_unlock_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 13
        self.white_list_http_method_settings.add(self.is_unlock_forward_requests_box, c)

    # 选项卡4-标签14-ui
    def tag_4_14(self, c):
        # 创建 检查框
        self.is_propfind_forward_requests_box = JCheckBox(u'转发PROPFIND请求', ForwardRequestsConfig.IS_PROPFIND_FORWARD_REQUESTS)
        self.setFontBold(self.is_propfind_forward_requests_box)
        self.is_propfind_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 14
        self.white_list_http_method_settings.add(self.is_propfind_forward_requests_box, c)

    # 选项卡4-标签15-ui
    def tag_4_15(self, c):
        # 创建 检查框
        self.is_view_forward_requests_box = JCheckBox(u'转发VIEW请求', ForwardRequestsConfig.IS_VIEW_FORWARD_REQUESTS)
        self.setFontBold(self.is_view_forward_requests_box)
        self.is_view_forward_requests_box.setForeground(Color(0, 0, 153))
        c.insets = Insets(5, 5, 5, 5)
        c.gridx = 0
        c.gridy = 15
        self.white_list_http_method_settings.add(self.is_view_forward_requests_box, c)

    # 获取白名单http方法
    def getWhiteListHttpMethod(self):
        l = []
        if self.is_get_forward_requests_box.isSelected():
            l.append('GET')
        if self.is_post_forward_requests_box.isSelected():
            l.append('POST')
        if self.is_put_forward_requests_box.isSelected():
            l.append('PUT')
        if self.is_patch_forward_requests_box.isSelected():
            l.append('PATCH')
        if self.is_delete_forward_requests_box.isSelected():
            l.append('DELETE')
        if self.is_copy_forward_requests_box.isSelected():
            l.append('COPY')
        if self.is_head_forward_requests_box.isSelected():
            l.append('HEAD')
        if self.is_options_forward_requests_box.isSelected():
            l.append('OPTIONS')
        if self.is_link_forward_requests_box.isSelected():
            l.append('LINK')
        if self.is_unlink_forward_requests_box.isSelected():
            l.append('UNLINK')
        if self.is_purge_forward_requests_box.isSelected():
            l.append('PURGE')
        if self.is_lock_forward_requests_box.isSelected():
            l.append('LOCK')
        if self.is_unlock_forward_requests_box.isSelected():
            l.append('UNLOCK')
        if self.is_propfind_forward_requests_box.isSelected():
            l.append('PROPFIND')
        if self.is_view_forward_requests_box.isSelected():
            l.append('VIEW')
        return l

class TextAreaMouseListener(MouseAdapter):
    def __init__(self, text_area):
        self.text_area = text_area

    def getSelected(self):
        return (self.start, self.value)

    def mousePressed(self, event):
        if event.getButton() != MouseEvent.BUTTON1:
            return

        offset = self.text_area.viewToModel(event.getPoint())
        rowStart = Utilities.getRowStart(self.text_area, offset)
        rowEnd = Utilities.getRowEnd(self.text_area, offset)
        self.start = rowStart
        self.value = self.text_area.getText()[rowStart: rowEnd]

        self.text_area.getHighlighter().removeAllHighlights()
        painter = DefaultHighlighter.DefaultHighlightPainter(Color.LIGHT_GRAY)
        self.text_area.getHighlighter().addHighlight(rowStart, rowEnd, painter)

class ButtonHandlers:
    def __init__(self, text_field, text_area, mouse_listener, default_values):
        self.text_field = text_field
        self.text_area = text_area
        self.mouse_listener = mouse_listener
        self.default_values = default_values

    def handler_add(self, event):
        name = self.text_field.getText()
        self.text_area.append(name + '\n' + os.linesep)
        self.text_field.setText('')

    def handler_rm(self, event):
        self.text_field.setText('')
        start, value = self.mouse_listener.getSelected()
        end = start + len(value)
        text_area = self.text_area.getText()
        text_area = (text_area[:start] + text_area[end:]).strip('\n').replace('\n\n', '\n')
        self.text_area.setText(text_area)

    def handler_restore(self, event):
        self.text_field.setText('')
        self.text_area.setText('')
        for name in self.default_values:
            self.text_area.append(name + '\n' + os.linesep)

