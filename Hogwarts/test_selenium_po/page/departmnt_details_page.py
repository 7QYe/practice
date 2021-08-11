"""
author : QY
"""
from test_selenium_po.page.base_page import BasePage


class DepartmentDetailsPage(BasePage):
    # 获取部门名
    def get_name(self, dname):
        self.find_by_id("memberSearchInput").send_keys(dname)
        search = self.driver.find_element_by_xpath("//*[@id='search_party_list']//a").text
        return search

    # 部门点开后的具体操作
    # 添加成员
    def department_details(self):
        from test_selenium_po.page.add_member_page import AddMemberPage
        self.find_by_class("qui_btn.ww_btn.js_add_member").click()
        return AddMemberPage(self.driver)

    # 批量导入
    def bulk_import(self):
        pass

    # 从其他部门移入
    def from_another_department(self):
        pass
