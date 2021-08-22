"""
author : QY
通讯录页面
"""

from selenium.webdriver.common.by import By

from appium_po_wechat.page.add_member_page import AddMemberPage
from appium_po_wechat.page.basepage import BasePage
from appium_po_wechat.page.person_info_page import PersonInfoPage
from appium_po_wechat.page.search_page import SearchPage


class ContactPage(BasePage):
    # 点击添加成员
    def click_add_member(self):
        self.swip_click("添加成员")
        return AddMemberPage(self.driver)

    # 点击成员，进入成员详情页
    def click_member(self, name):
        self.swip_click(name)
        return PersonInfoPage(self.driver)

    # 点击搜索按钮，搜索成员
    def click_search(self):
        self.find_click(By.XPATH, "//*[@resource-id='com.tencent.wework:id/it6']")
        return SearchPage(self.driver)
