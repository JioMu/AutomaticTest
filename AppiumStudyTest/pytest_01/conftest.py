import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 全局变量(模块级别)
_driver = None


@pytest.fixture(scope="module")
def appium_driver(request):
    global _driver
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.device_name = 'k71v1_64_bsp'
    options.automation_name = 'UiAutomator2'
    options.platform_version = "11"
    # options.app_package = 'io.meehoo.eleinspect'
    # options.app_activity = "io.dcloud.PandoraEntryActivity"
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    """class级别变量"""
    # request.cls.driver = driver
    # yield driver
    # driver.quit()
    _driver = driver
    yield _driver
    _driver.quit()
