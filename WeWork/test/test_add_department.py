"""
author : QY
"""

from page.main_page import MainPage
from test.utils import Utils


class TestAddDepartment:
    def setup(self):
        self.main_page = MainPage()
        self.utils = Utils()

    def test_add_department(self):
        dname = self.utils.get_department()
        dinfo = self.main_page.goto_add_member().add_department(dname)

        """
        断言：取随机生成的部门名称与部门详情页的名称断言（部门名称是唯一的）
        """
        # 传入参数另赋值
        sear = dname
        assert dinfo.get_name(sear) == dname
