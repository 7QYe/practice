"""
author : QY
"""
from selenium.webdriver.common.by import By

from appium_po_wechat.page.basepage import BasePage
from appium_po_wechat.page.person_info_more_page import PersonInfoMorePage


class PersonInfoPage(BasePage):
    # 点击右上角 功能按钮
    def click_more(self):
        self.find_click(By.XPATH, "//*[@text='个人信息']/../../../../..//*[@resource-id='com.tencent.wework:id/it_']")
        return PersonInfoMorePage(self.driver)
