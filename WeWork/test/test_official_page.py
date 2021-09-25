"""
author : QY
"""
from page.official_page import OfficialPage
from test.utils import Utils


class TestOfficialPage:
    def setup(self):
        self.official = OfficialPage()
        self.utils = Utils()
        self.corp_name = self.utils.get_corp_name()
        self.mname = self.utils.get_username()
        self.tel = self.utils.get_phone()
        # 生成随机6位数字
        self.vcode = self.utils.get_random_number(6)

    def test_goto_login(self):
        self.official.goto_login().scan()

    def test_goto_register(self):
        self.official.goto_register().register(self.corp_name, self.mname, "18739933511", self.vcode)
        self.official.goto_register().find_message()


    def test_goto_login_register(self):
        self.official.goto_register().goto_register().register(self.corp_name, self.mname, "18739933511", self.vcode)

    def test_download_win(self):
        self.official.goto_download_page().download_win()

    def test_download_mac(self):
        self.official.goto_download_page().download_mac()

    def test_download_ios(self):
        self.official.goto_download_page().download_ios()

    def test_download_android(self):
        self.official.goto_download_page().download_android()
