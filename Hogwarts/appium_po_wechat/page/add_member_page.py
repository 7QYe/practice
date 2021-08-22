"""
author : QY
添加成员页面
"""
from selenium.webdriver.common.by import By
from appium_po_wechat.page.basepage import BasePage
from appium_po_wechat.page.editor_member_page import EditorMemberPage


class AddMemberPage(BasePage):
    def add_member(self):
        # 点击手动输入添加
        self.find_click(By.XPATH, "//*[@text='手动输入添加']")
        return EditorMemberPage(self.driver)

    def find_toast(self):
        # 寻找toast
        add = self.find(By.XPATH, "//*[contains(@text,'添加成功')]")
        return add
