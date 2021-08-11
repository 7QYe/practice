"""
author : QY
"""
from test_selenium_po.page.base_page import BasePage
from test_selenium_po.page.contacts_page import ContactsPage
from test_selenium_po.page.departmnt_details_page import DepartmentDetailsPage


class AddMemberPage(BasePage):
    """
    添加成员
    """

    def add_member(self, username, acctid, phone):
        """
        添加成员
        :param username: 姓名
        :param acctid: 别名唯一id
        :param phone: 手机号
        :return:
        """
        self.find_by_id("username").send_keys(username)
        self.find_by_id("memberAdd_acctid").send_keys(acctid)
        self.find_by_id("memberAdd_phone").send_keys(phone)
        self.find_by_class("js_btn_continue").click()
        return ContactsPage(self.driver)

    """
    添加部门
    """

    def add_department(self, dname):
        # 点击搜索框旁的+号 弹出添加部门对话框
        self.find_by_class("js_create_dropdown").click()
        self.find_by_class("js_create_party").click()

        # div弹框要二次定位，先定位所选元素在的div标签，再定位此元素
        popup = self.find_by_id("__dialog__MNDialog__")
        popup.find_element_by_class_name("qui_inputText.ww_inputText").send_keys(dname)

        # 点击下拉列表
        popup.find_element_by_class_name("qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list").click()
        # 选择第一个部门选项
        lis = self.find_by_class("jstree.jstree-2.jstree-default")
        lis.find_element_by_class_name("jstree-anchor").click()
        # 点击确认按钮
        popup.find_element_by_class_name("qui_btn.ww_btn.ww_btn_Blue").click()
        # 返回添加部门后的 部门详情界面
        return DepartmentDetailsPage(self.driver)
