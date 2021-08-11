"""
author : QY
"""

import random
from test_selenium_po.page.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main_page = MainPage()

    # 重复执行用例，括号内为重新执行的次数
    # @pytest.mark.repeat(3)
    def test_add_member(self):
        """
        生成随机用户名
        :return:
        """
        first_name = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        last_name = '贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹富顺信子杰涛昌成康星光天达安岩中茂进林有坚和'
        F = random.choice(first_name)
        L = "".join(random.choice(last_name) for i in range(2))
        username = F + L

        """
        生成随机账号
        """
        id = ''.join(random.sample("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 8))

        """
        生成随机手机号
        第1位数字是1
        第2位数字是，3，4，5，7，8
        第3位数字根据不同运营商的规则，随机选出
        """
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(1, 4)]
        # 第三位数字
        third = {3: random.randint(0, 9),
                 4: [5, 7, 9][random.randint(0, 2)],
                 5: [i for i in range(10) if i != 4][random.randint(0, 8)],
                 7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
                 8: random.randint(0, 9), }[second]
        # 最后八位数字
        suffix = random.randint(9999999, 100000000)
        # 拼接成手机号
        phone = "1{}{}{}".format(second, third, suffix)
        # 调用方法，传入信息
        info = self.main_page.goto_add_member().add_member(username, id, phone)

        """
        断言：根据手机号的唯一性进行断言，搜索出添加的成员信息，与随机生成的成员信息进行断言操作
        """
        # 在通讯录输入要查询的成员名，在成员详情页获取到手机号，再与随机生成的手机号进行断言
        # 获取手机号
        # 传入的参数另赋值
        sname = username
        assert info.find_message(sname).get_phone() == phone
