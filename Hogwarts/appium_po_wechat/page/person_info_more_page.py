"""
author : QY
"""
from selenium.webdriver.common.by import By
from appium_po_wechat.page.basepage import BasePage
from appium_po_wechat.page.revise_member_page import ReviseMemberPage


class PersonInfoMorePage(BasePage):
    def click_editor(self):
        # 点击 编辑成员 按钮
        self.find_click(By.XPATH, "//*[@text='编辑成员']")
        return ReviseMemberPage(self.driver)
