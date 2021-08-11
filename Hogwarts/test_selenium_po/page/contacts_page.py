"""
author : QY
"""
from test_selenium_po.page.base_page import BasePage
from test_selenium_po.page.member_details_page import MemberDetailsPage


class ContactsPage(BasePage):
    def find_message(self,sname):
        # 输入想查询的成员
        self.find_by_class("qui_inputText.ww_inputText.ww_searchInput_text").send_keys(sname)
        # 获取到展示的页面
        return MemberDetailsPage(self.driver)