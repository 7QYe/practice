"""
author : QY
"""
from time import sleep

from page.basepage import BasePage


class RegisterPage(BasePage):

    #
    def register(self, corp_name, mname, retel, vcode):
        # 企业名称
        self.send_keys_by_id("corp_name", corp_name)
        # 选择行业类型 IT服务 计算机硬件软件信息服务
        self.click_by_xpath(
            "//*[@class='qui_btn ww_btn ww_btn_Big ww_btn_Block ww_btn_Dropdown js_corp_industry_btn']")
        self.click_by_xpath("//*[@id='corp_industry']//div//*[@data-name='IT服务']")
        self.click_by_xpath("//*[@id='corp_industry']//div//*[@data-name='计算机软件/硬件/信息服务']")

        # 选择员工规模 1-50人
        self.click_by_xpath("//*[@id='corp_scale_btn']")
        self.click_by_xpath("//*[@id='corp_scale_btn']//li[1]")

        # 管理员姓名
        self.send_keys_by_id("manager_name", mname)
        self.send_keys_by_id("register_tel", retel)

        # 获取验证码 填写验证码
        self.click_by_id("get_vcode")
        # 等待手动验证
        sleep(5)
        self.send_keys_by_id("vcode", vcode)
        # 同意协议
        self.click_by_id("iagree")
        # 点击注册
        self.click_by_id("submit_btn")



