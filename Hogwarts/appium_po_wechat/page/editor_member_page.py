"""
author : QY
编辑成员信息页面
"""
from faker import Faker
from selenium.webdriver.common.by import By

from appium_po_wechat.page.basepage import BasePage
from appium_po_wechat.utils.get_data import GetData


class EditorMemberPage(BasePage):
    def editor_member(self,name,phone):
        from appium_po_wechat.page.add_member_page import AddMemberPage
        # 填写姓名
        self.find_send(By.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText", name)
        # 填写手机号
        self.find_send(By.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText", phone)
        # 点击保存
        self.find_click(By.XPATH, "//*[@text='保存']")
        return AddMemberPage(self.driver)
