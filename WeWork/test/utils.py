"""
author : QY
"""
import random

from faker import Faker


class Utils():
    def __init__(self):
        self.f = Faker(locale='zh_CN')

    def get_username(self):
        """
        生成随机用户名
        :return:
        """
        first_name = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        last_name = '贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹富顺信子杰涛昌成康星光天达安岩中茂进林有坚和'
        F = random.choice(first_name)
        L = "".join(random.choice(last_name) for i in range(2))
        username = F + L
        return username

    def get_enname(self):
        enname = self.f.name()
        return enname

    def get_accid(self):
        """
               生成随机账号
        """
        id = ''.join(random.sample("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 8))
        return id

    def get_phone(self):
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

        return phone

    def get_telephone(self):
        telephone = self.f.phone_number()
        return telephone

    def get_mail(self):
        mail = self.f.email()
        return mail

    def get_address(self):
        address = self.f.address()
        return address

    def get_title(self):
        title = self.f.job()
        return title

    def get_department(self):
        d_first = random.choice(["运营", "产品", "设计", "测试", "研发"])
        dname = d_first + "部"
        return dname

    def get_corp_name(self):
        corp_name = self.f.company()
        return corp_name

    # 生成随机数字 参数为生成的数字位数
    def get_random_number(self, digtial):
        num = self.f.random_number(digtial)
        return num
