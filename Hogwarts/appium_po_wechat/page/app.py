"""
author : QY
"""
from time import sleep
from appium import webdriver
from appium_po_wechat.page.basepage import BasePage
from appium_po_wechat.page.main_page import MainPage


# app的相关操作
class App(BasePage):
    def start(self):
        if self.driver == None:
            print("qidong app")
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
        else:
            print("launch 启动app")
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        pass

    def goto_main(self):
        sleep(10)
        return MainPage(self.driver)
