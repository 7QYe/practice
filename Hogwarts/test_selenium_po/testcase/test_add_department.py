"""
author : QY
"""
import random

from test_selenium_po.page.main_page import MainPage


class TestAddDepartment:
    def setup(self):
        self.main_page = MainPage()

    def test_add_department(self):
        d_first = random.choice(["运营", "产品", "设计", "测试", "研发"])
        dname = d_first + "部"
        dinfo = self.main_page.goto_add_member().add_department(dname)

        """
        断言：取随机生成的部门名称与部门详情页的名称断言（部门名称是唯一的）
        """
        # 传入参数另赋值
        sear = dname
        assert dinfo.get_name(sear) == dname
