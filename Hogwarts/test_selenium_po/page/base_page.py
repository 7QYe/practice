"""
author : QY
1.子类主动调用__init__
3,冒号：代表注解 语法提示，本身没有代码作用
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # 默认访问这个路径，但是子类有声明就会用子类的
    URL = "https://work.weixin.qq.com/"

    def __init__(self, driver: WebDriver = None):
        # 如果driver是None就初始化，如果不是None
        if not driver:
            option = Options()
            option.debugger_address = "localhost:9222"

            self.driver = webdriver.Chrome(options=option)
            self.driver.get(self.url)
            self.driver.implicitly_wait(5)
        #     如果是第二次传递driver，

        else:
            self.driver = driver

    def find_by_id(self, id):
        """
        通过id进行查找
        :param id:
        :return:
        """
        return self.driver.find_element_by_id(id)

    def find_by_class(self,cls):
        """
        通过class进行查找
        :param cls:
        :return:
        """
        return self.driver.find_element_by_class_name(cls)
