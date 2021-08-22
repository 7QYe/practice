"""
author : QY
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    def __init__(self, driver: WebDriver = None):
        print("继承 basepage")
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        return self.driver.find_element(by, locator).click()

    def find_send(self, by, locator, text):
        return self.driver.find_element(by, locator).send_keys(text)

    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()
