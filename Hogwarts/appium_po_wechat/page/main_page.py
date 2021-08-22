"""
author : QY
主页
"""
from selenium.webdriver.common.by import By

from appium_po_wechat.page.basepage import BasePage
from appium_po_wechat.page.contact_page import ContactPage


class MainPage(BasePage):
    def click_contact(self):
        self.find_click(By.XPATH, "//*[@text='通讯录']")
        return ContactPage(self.driver)
