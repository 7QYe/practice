"""
author : QY
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    # 默认访问的路径
    URL = "https://work.weixin.qq.com/"

    def __init__(self, driver: WebDriver = None):
        if not driver:
            option = Options()
            option.debugger_address = "localhost:9222"

            self.driver = webdriver.Chrome(options=option)
            # self.driver.get(self.url)
            self.driver.get("https://work.weixin.qq.com/")
            self.driver.implicitly_wait(5)

        else:
            self.driver = driver

    def find_by_id(self, id):
        '''
        通过id进行查找
        :param id:
        :return:
        '''
        return self.driver.find_element_by_id(id)

    def find_by_class(self, cls):
        '''
        通过class进行查找
        :param cls:
        :return:
        '''
        return self.driver.find_element_by_class_name(cls)

    def find_by_xpath(self, xpath):
        '''
        通过xpath进行查找
        :param xpath:
        :return:
        '''
        return self.driver.find_element_by_xpath(xpath)

    def click_by_id(self, id):
        return self.find_by_id(id).click()

    def click_by_xpath(self, xpath):
        return self.find_by_xpath(xpath).click()

    def click_by_class(self, cls):
        return self.find_by_class(cls).click()

    def send_keys_by_id(self, id, text):
        return self.find_by_id(id).send_keys(text)

    def send_keys_by_class(self, cls, text):
        return self.find_by_class(cls).send_keys(text)

    def send_keys_by_xpath(self, xpath, text):
        return self.find_by_xpath(xpath).send_keys(text)
