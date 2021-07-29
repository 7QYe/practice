"""
author : QY
work : 复用浏览器 添加成员
"""
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWechatRemote:
    # 打开企业微信页面
    # 复用浏览器，注意先关闭所有chrome，在cmd中输入chrome --remote-debugging-port=9222，打开pycharm执行代码
    def test_remote_chrome(self):
        # 复用浏览器
        # 实例化 options
        option = Options()
        # 设置端口连接
        option.debugger_address = "localhost:9222"
        # 实例化driver 不要忘了()的内容
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        # 网页跳转有时速度慢，设置的时间稍微长些
        sleep(5)

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


