"""
author : QY
"""
from page.basepage import BasePage
from page.member_details_page import MemberDetailsPage


class ContactsPage(BasePage):
    def find_message(self, sname):
        # 输入想查询的成员信息
        self.send_keys_by_class("qui_inputText.ww_inputText.ww_searchInput_text", sname)
        return MemberDetailsPage(self.driver)
