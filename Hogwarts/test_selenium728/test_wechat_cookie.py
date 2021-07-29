"""
author : QY
work : Cookie 添加成员
"""
from time import sleep

import yaml
from selenium import webdriver


class TestWechatCookie:

    def test_cookie_get(self):
        self.driver = webdriver.Chrome()
        # 进入页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        # 进入后 手动扫码 首先存储一个cookie的数据
        sleep(25)
        # 存储上一步扫码登录的cookie值，存储到yaml中
        cookie_var = self.driver.get_cookies()
        sleep(5)
        yaml.safe_dump(cookie_var, open("wechat.yml", mode="w", encoding="utf-8"))

    def test_cookie_login(self):
        # 获取cookie的值
        cookies = yaml.safe_load(open("wechat.yml", encoding="utf-8"))
        # 打开网页 在输入cookie
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 写入cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        sleep(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        self.driver.find_element_by_css_selector(".ww_indexImg_AddMember").click()
        sleep(5)
        # 获取姓名输入框 输入内容
        # 【获取表单输入框元素后需要点击 才可以输入内容】
        self.driver.find_element_by_class_name("ww_compatibleTxt_ipt").click()
        self.driver.find_element_by_class_name("ww_compatibleTxt_ipt").send_keys("fairytale2")
        # 输入账号
        self.driver.find_element_by_id("memberAdd_acctid").click()
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("fairy2")
        # 输入手机号
        self.driver.find_element_by_id("memberAdd_phone").click()
        self.driver.find_element_by_id("memberAdd_phone").send_keys("18733399999")
        # 定位css元素时，中间用.分隔开
        self.driver.find_element_by_css_selector("a.qui_btn.ww_btn.js_btn_save").click()

