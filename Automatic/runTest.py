import time
from selenium.webdriver.common.by import By
from Utils.webDriverUtils import WebDriverOpen
# 显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == "__main__":
    try:
        # 初始化 WebDriver 实例
        web_driver_utils = WebDriverOpen("谷歌")

        # 获取 WebDriver 实例
        driver = web_driver_utils.driver

        # 访问百度首页
        driver.get("https://www.baidu.com")
        driver.maximize_window()
        # 查找搜索框并输入关键词
        element_present = EC.presence_of_element_located((By.NAME, "wd"))
        if element_present:
            search_box = WebDriverWait(driver, 10).until(element_present)
        search_box.send_keys("Selenium Python")
        search_box.submit()

        # 等待页面加载
        time.sleep(3)

    except Exception as e:
        print(f"操作失败: {e}")

    finally:
        # 关闭浏览器
        if driver:
            driver.quit()
