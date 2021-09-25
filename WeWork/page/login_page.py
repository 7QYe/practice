"""
author : QY
"""
from page.basepage import BasePage
from page.register_page import RegisterPage


class LoginPage(BasePage):
    def scan(self):
        '''

        :return:
        '''
        pass

    def goto_register(self):
        '''

        :return:
        '''
        self.find_by_xpath("//*[@class='login_registerBar_link']").click()
        return RegisterPage(self.driver)
