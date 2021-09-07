"""
author : QY
"""
import allure

from test_requests.apis.tag import Tag
from test_requests.testcase.utils import Utils


@allure.feature("标签管理")
class TestTag:
    def setup(self):
        # 获取access_token
        datas = Utils.get_data_yaml("../data/config.yaml")
        corpid = datas["corpid"]["qy"]
        corpsecret = datas["secret"]["label_secret"]

        # 实例化标签类
        self.tag = Tag(corpid, corpsecret)

        # 清除标签信息
        self.tag.clear_tag()

        # 准备测试数据
        self.tag_id = 12

        # 创建标签的数据
        self.create_data = {
            "tagname": "UI",
            "tagid": self.tag_id
        }
        self.create_data1 = {
            "tagname": "UITEST1111",
            "tagid": 10
        }

        # 增加标签成员数据
        self.add_user_data = {
            "tagid": self.tag_id,
            "userlist": ["tutu", "tutu01", "XingXingXi"],
            "partylist": [2]
        }

        # 删除标签成员数据
        self.delete_user_data = {
            "tagid": self.tag_id,
            "userlist": ["tutu", "tutu01"],
            "partylist": [2]
        }

        # 更新的数据
        self.update_data = {
            "tagid": self.tag_id,
            "tagname": "UI design"
        }

    @allure.story("标签操作场景用例")
    def test_tag_scene(self):
        '''
        标签增删改查 场景测试
        :return:
        '''

        # 创建标签
        with allure.step("创建标签"):
            self.tag.creat_tag(self.create_data)
            self.tag.creat_tag(self.create_data1)
        # 断言
        with allure.step("验证标签是否创建成功"):
            l = self.tag.get_tags()
            tagname_list = Utils.base_jsonpath(l, "$..tagname")
            print(tagname_list)
            assert "UI" in tagname_list

        # 添加标签成员
        with allure.step("添加标签成员"):
            self.tag.add_tag_user(self.add_user_data)
        with allure.step("验证添加成员成功"):
            user = self.tag.get_tag_user(self.tag_id)
            userid_list = Utils.base_jsonpath(user, "$..userid")
            print(userid_list)
            for i in range(0, len(self.add_user_data["userlist"])):
                assert self.add_user_data["userlist"][i] in userid_list
                i += 1

        # 删除标签成员
        with allure.step("删除标签成员"):
            self.tag.delete_tag_user(self.delete_user_data)
        with allure.step(("验证删除成员成功")):
            del_user = self.tag.get_tag_user(self.tag_id)
            del_userid_list = Utils.base_jsonpath(del_user, "$..userid")
            print(del_userid_list)
            for i in range(0, len(self.delete_user_data["userlist"])):
                assert self.delete_user_data["userlist"][i] not in del_userid_list
                i += 1
            print()

        # 更新标签
        with allure.step("更新标签信息"):
            self.tag.update_tag(self.update_data)
        # 断言
        with allure.step("验证标签是否更新成功"):
            l = self.tag.get_tags()
            tagname_list = Utils.base_jsonpath(l, "$..tagname")
            print(tagname_list)
            assert "UI design" in tagname_list

        # 删除标签
        with allure.step("删除指定标签"):
            self.tag.delete_tag(self.tag_id)
        # 断言
        with allure.step("验证是否删除成功"):
            # 获取列表中所有的标签信息
            l = self.tag.get_tags()
            # 获取 标签名 列表
            tagname_list = Utils.base_jsonpath(l, "$..tagname")
            print(tagname_list)
            # 判断 删除的标签名 是否还在列表中（标签名不能重复）
            # 列表为空返回false，先判断是否为空，为空不能遍历
            if tagname_list is False:
                print("该列表为空,无需删除")
            else:
                assert "UI design" not in tagname_list
