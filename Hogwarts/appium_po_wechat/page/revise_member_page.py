"""
author : QY
"""
from selenium.webdriver.common.by import By

from appium_po_wechat.page.basepage import BasePage


class ReviseMemberPage(BasePage):
    def delete_member(self):
        from appium_po_wechat.page.contact_page import ContactPage
        # 滑动查找，点击删除成员
        self.swip_click("删除成员")
        # 点击确定按钮
        self.find_click(By.XPATH, "//*[@text='确定']")
        return ContactPage(self.driver)
