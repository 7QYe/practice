"""
author : QY
"""

from page.main_page import MainPage
from test.utils import Utils


class TestAddMember:
    def setup(self):
        self.main_page = MainPage()
        self.utils = Utils()
        # 重复执行用例，括号内为重新执行的次数
        # @pytest.mark.repeat(3)

    def test_add_member(self):
        # 使用工具类，生成测试数据
        username = self.utils.get_username()
        enname = self.utils.get_enname()
        acctid = self.utils.get_accid()
        phone = self.utils.get_phone()
        telephone = self.utils.get_telephone()
        mail = self.utils.get_mail()
        address = self.utils.get_address()
        title = self.utils.get_title()

        # 调用方法，传入信息
        info = self.main_page.goto_add_member().add_member(username, enname, acctid, phone, telephone, mail, address,
                                                           title)

        """
        断言：根据手机号的唯一性进行断言，搜索出添加的成员信息，与随机生成的成员信息进行断言操作
        """
        # 在通讯录输入要查询的成员名，在成员详情页获取到手机号，再与随机生成的手机号进行断言
        # 获取手机号
        # 传入的参数另赋值
        sname = username
        assert info.find_message(sname).get_phone() == phone
