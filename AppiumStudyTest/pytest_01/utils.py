import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化参数
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "11.0"
options.device_name = "emulator-5554"
options.app = "D:\\appium\\app\\app-release.apk"


class Utils:
    def __init__(self, driver):
        # 初始化driver
        self.driver = driver
        # 设置显示等待时间
        self.wait = WebDriverWait(self.driver, 10)

    def find_element_EC(self, locator, method):
        """增强定位方法"""
        by_map = {
            "id": lambda: EC.presence_of_element_located((AppiumBy.ID, locator)),
            "xpath": lambda: EC.presence_of_element_located((AppiumBy.XPATH, locator))
        }
        if method.lower() not in by_map:
            raise ValueError(f"不支持的定位方式: {method}")
        return self.wait.until(by_map[method.lower()]())

        # match method:
        #     case "id":
        #         return self.wait.until(EC.presence_of_element_located((AppiumBy.ID, locator)))
        #     case "xpath":
        #         return self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, locator)))

    # def find_element(self, locator, method):
    #     match method:
    #         case "id":
    #             return self.driver.find_element(AppiumBy.ID, locator)
    #         case "xpath":
    #             return self.driver.find_element(AppiumBy.XPATH, locator)
