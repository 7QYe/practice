"""
author : QY
"""
from test_selenium_po.page.base_page import BasePage


class MemberDetailsPage(BasePage):

    def get_phone(self):
        # 获取到查询成员的具体信息
        # 获取手机号
        ph1 = self.driver.find_element_by_xpath(
            '//*[@class="member_display_item member_display_item_Phone"]//div[2]').text
        print(ph1)
        return ph1
