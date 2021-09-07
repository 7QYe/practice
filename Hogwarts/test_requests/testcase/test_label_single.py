"""
author : QY
"""
import allure
import pytest

from test_requests.apis.tag import Tag
from test_requests.testcase.utils import Utils


@allure.feature("标签管理 单接口测试")
class TestLabelSingle:
    '''
    创建标签的单接口测试
    '''

    def setup_class(self):
        # 获取token
        token_datas = Utils.get_data_yaml("../data/config.yaml")
        corpid = token_datas["corpid"]["qy"]
        corpsecret = token_datas["secret"]["label_secret"]

        # 实例化标签类
        self.tag = Tag(corpid, corpsecret)

    # 准备测试数据，从yaml文件中读取数据
    tag_datas = Utils.get_data_yaml("../data/create.yaml")

    @allure.story("标签名输入验证")
    @pytest.mark.parametrize(
        "tagname,tagid,expect",
        tag_datas["datas"],
        ids=tag_datas["ids"]
    )
    def test_create_tag(self, tagname, tagid, expect):
        data = {
            "tagname": tagname,
            "tagid": tagid
        }
        r = self.tag.creat_tag(data)
        assert r["errcode"] == expect
