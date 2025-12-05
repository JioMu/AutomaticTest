import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import utils


@pytest.mark.usefixtures("appium_driver")
class TestCase1:
    """
    测试用例1
    """

    @classmethod
    def setup_class(cls, request):
        cls.driver = request.module.driver

    def setup_method(self):
        self.wait = WebDriverWait(self.driver, 10)
        utils.Utils(self.driver).find_element_EC('//android.widget.TextView[@content-desc="检验影像"]', 'xpath').click()
        assert utils.Utils(self.driver).find_element_EC('//android.widget.TextView[@text="电梯影像"]', 'xpath')
        print("进入检验影像app")

    def teardown_method(self):
        time.sleep(60)
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.quit()
        print("退出检验影像app")

    def test_login(self):
        try:
            utils.Utils(self.driver).find_element_EC(
                '(//android.view.View[@resource-id="app"])[2]/android.view.View/android.view.View[3]/android.view.View['
                '2]/android.view.View/android.view.View/android.widget.EditText',
                'xpath').send_keys(
                "罗斯")
            utils.Utils(self.driver).find_element_EC(
                '(//android.view.View[@resource-id="app"])[2]/android.view.View/android.view.View[4]/android.view.View['
                '2]/android.view.View/android.view.View/android.widget.EditText',
                'xpath').send_keys(
                "LUOsi1616*")
            utils.Utils(self.driver).find_element_EC('//android.widget.TextView[@text="点击完成验证"]', 'xpath').click()
            time.sleep(5)
            utils.Utils(self.driver).find_element_EC('//android.widget.TextView[@text="登 录"]', 'xpath').click()
            assert utils.Utils(self.driver).find_element_EC('(//android.widget.TextView[@text="任务池"])[2]', 'xpath')
        except Exception as e:
            print({e}, "元素查找失败，排查报错")
