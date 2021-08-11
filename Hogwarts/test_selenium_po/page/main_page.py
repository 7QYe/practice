"""
author : QY
"""

from test_selenium_po.page.base_page import BasePage


class MainPage(BasePage):
    url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        from test_selenium_po.page.add_member_page import AddMemberPage
        self.driver.find_element_by_xpath("//*[@node-type='addmember']").click()
        return AddMemberPage(self.driver)

    def goto_import_address(self):
        pass

    def goto_join_member(self):
        pass
