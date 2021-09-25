"""
author : QY
"""
from page.basepage import BasePage
from page.download_page import DownloadPage
from page.login_page import LoginPage
from page.register_page import RegisterPage


class OfficialPage(BasePage):
    def goto_login(self):
        self.find_by_xpath("//*[@class='index_top_operation_loginBtn']").click()
        return LoginPage(self.driver)

    def goto_register(self):
        self.find_by_xpath("//*[@class='index_head_info_pCDownloadBtn']").click()
        return RegisterPage(self.driver)

    def goto_download_page(self):
        self.find_by_class("index_top_operation_registerBtn").click()
        return DownloadPage(self.driver)
