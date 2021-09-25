"""
author : QY
"""
from page.basepage import BasePage
from page.contacts_page import ContactsPage
from page.department_details_page import DepartmentDetailsPage


class AddMemberPage(BasePage):
    def add_member(self, username, enname, acctid, phone, telephone, mail, address, title):
        """
        添加成员
        :param username:姓名
        :param enname: 别名
        :param acctid: 账号
        :param phone: 手机号
        :param telephone: 座机
        :param mail: 邮箱
        :param address: 地址
        :param title: 职务
        :return:
        """
        self.send_keys_by_id("username", username)
        self.send_keys_by_id("memberAdd_english_name", enname)
        self.send_keys_by_id("memberAdd_acctid", acctid)
        # 选女
        self.click_by_xpath('//*[@name="gender"]//..//*[@value="2"]')
        # 选男
        # self.click_by_xpath('//*[@name="gender"]//..//*[@value="1"]')
        self.send_keys_by_id("memberAdd_phone", phone)
        self.send_keys_by_id("memberAdd_telephone", telephone)
        self.send_keys_by_id("memberAdd_mail", mail)
        self.send_keys_by_id("memberEdit_address", address)
        self.send_keys_by_id("memberAdd_title", title)
        # 选普通成员
        self.click_by_xpath('//*[@name="identity_stat"]//..//*[@value="0"]')
        # 选上级
        # self.click_by_xpath('//*[@name="identity_stat"]//..//*[@value="1"]')
        # 选同步公司内职务
        self.click_by_xpath('//*[@name="extern_position_set"]//..//*[@value="sync"]')
        # 选自定义
        # self.click_by_xpath('//*[@name="extern_position_set"]//..//*[@value="custom"]')

        # 通过邮件发送企业邀请
        self.click_by_xpath("//*[@name='sendInvite']")
        # 保存并继续添加
        self.click_by_class("js_btn_continue")
        # 保存
        # self.click_by_class("js_btn_save")
        # 取消
        # self.click_by_class("js_btn_cancel")
        return ContactsPage(self.driver)

    def add_department(self, dname):
        """
        添加部门
        :param dname:
        :return:
        """
        # 点击搜索框旁的+号 弹出添加部门对话框
        self.click_by_class("js_create_dropdown")
        self.click_by_class("js_create_party")

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
