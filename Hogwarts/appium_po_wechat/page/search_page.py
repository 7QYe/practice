"""
author : QY
"""
from selenium.webdriver.common.by import By

from appium_po_wechat.page.basepage import BasePage


class SearchPage(BasePage):
    def search_member(self,name):
        # 搜索已删除的成员名字
        self.find_send(By.XPATH, "//*[@resource-id='com.tencent.wework:id/hd5']", name)
        # 返回界面信息，是否有结果
        dele = self.find(By.XPATH, "//*[@text='无搜索结果']")
        return dele
