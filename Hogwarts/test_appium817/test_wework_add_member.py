"""
author : QY
"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker


class TestWeWork:
    def setup(self):
        caps = {}
        # 设置app的平台
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        # app包名
        caps["appPackage"] = "com.tencent.wework"
        # app启动页
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空缓存
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间为0秒
        caps['settings[waitForIdleTimeout]'] = 0

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

    def teardowm(self):
        self.driver.quit()

    def test_add_member(self):
        # 使用Faker库生成随机姓名和手机号
        # 实例化一个Faker对象
        faker = Faker(locale='zh_CN')
        # 调用Faker生成随机姓名、手机号的方法
        name = faker.name()
        phone = faker.phone_number()
        # 点击通讯录
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        # 滑动 查找添加成员元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        # 点击手动输入添加
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()

        # 填写姓名
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # 填写手机号
        self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(
            phone)
        # 点击保存
        self.driver.find_element_by_xpath("//*[@text='保存']").click()

        # 断言 是否有toast弹框
        add = self.driver.find_element_by_xpath("//*[@text='添加成功']")
        assert add
