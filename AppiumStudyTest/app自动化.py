from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 方法一：使用 load_capabilities（确保路径正确）
# capabilities = UiAutomator2Options.load_capabilities("path/to/caps.json")

# 方法二：推荐方式，直接构建 options
options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = '23117RK66C'
options.automation_name = 'UiAutomator2'
options.platform_version = "12"
options.app_package = 'com.android.settings'
options.app_activity = ".Settings"


class StudyAppium:
    def __init__(self):
        # 初始化driver
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        # 设置显示等待时间
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator, method):
        match method:
            case "id":
                return self.driver.find_element(AppiumBy.ID, locator)
            case "xpath":
                return self.driver.find_element(AppiumBy.XPATH, locator)

    def test_app(self):
        try:
            self.wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.android.settings:id/homepage_container")))
            print("进入设置页面")

            network_option = self.find_element('//android.widget.TextView[@resource-id="android:id/title" and '
                                               '@text="网络和互联网"]', "xpath")
            print("点击网络和互联网", network_option)
            network_option.click()

        except Exception as e:
            print("未找到元素")


if __name__ == '__main__':
    study_appium = StudyAppium()
    study_appium.test_app()
