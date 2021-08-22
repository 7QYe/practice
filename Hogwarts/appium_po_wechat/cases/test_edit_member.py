"""
author : QY
"""
import pytest

from appium_po_wechat.page.app import App
from appium_po_wechat.utils.get_data import GetData


class TestEditMember:
    # 类中只执行一次
    def setup_class(self):
        self.app = App()

    def setup(self):
        # 启动app
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    # 参数化用例 添加成员
    @pytest.mark.parametrize('name,phone', [('星星西', '18736655221')])
    def test_add_member(self, name, phone):
        # # 调用工具类生成随机姓名、手机号的方法
        # name = GetData().get_name()
        # phone = GetData().get_phone()
        ele = self.main.click_contact().click_add_member().add_member().editor_member(name, phone).find_toast()
        # 断言
        assert ele

    # 参数化用例 删除成员
    @pytest.mark.parametrize('name', ['星星西'])
    def test_delete_member(self, name):
        delet = self.main.click_contact().click_member(
            name).click_more().click_editor().delete_member().click_search().search_member(name)
        # 断言 是否有搜索结果，即删除是否成功
        assert delet
