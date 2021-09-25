"""
author : QY
"""
from page.app_apple_page import AppApplePage
from page.basepage import BasePage


class DownloadPage(BasePage):
    def download_win(self):
        '''
        下载windows桌面端
        :return:
        '''
        self.click_by_class("index_download_item.index_download_item_Window")

    def download_mac(self):
        '''
        下载mac桌面端
        :return:
        '''
        self.click_by_xpath("//*[@class='index_download_item index_download_item_Mac']")

    def download_ios(self):
        '''
        下载ios版本
        :return:
        '''
        self.click_by_class("index_download_item_iconWrap")
        # 跳转AppleStore商店预览
        return AppApplePage(self.driver)

    def download_android(self):
        '''
        下载Android版
        :return:
        '''
        self.click_by_class("index_download_item")
