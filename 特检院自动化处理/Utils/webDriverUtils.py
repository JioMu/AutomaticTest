from selenium import webdriver
from selenium.webdriver import Chrome as ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FireFoxService

from selenium.webdriver import Edge as EdgeDriver
from selenium.webdriver import Firefox as FirefoxDriver
from webdriver_manager.chrome import ChromeDriverManager  # 谷歌驱动
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # edge驱动
from webdriver_manager.firefox import GeckoDriverManager  # 火狐驱动

import time

'''不同的浏览器的打开方法'''


class WebDriverOpen:
    def __init__(self, web_type):
        self.web_type = web_type
        self.driver = self.installDriver()

    # 安装浏览器驱动启动浏览器
    def installDriver(self):
        print("开始安装驱动" + self.web_type)
        start_time = time.time()
        driver = None
        try:
            match self.web_type:
                case "google_chrome":
                    manager = ChromeDriverManager()
                    service = ChromeService(executable_path=manager.install())
                    driver = webdriver.Chrome(service=service)
                    end_time = time.time()
                    print("Chrome驱动安装完成,"+"耗时:"+str(end_time-start_time)+"秒")
                case 'edge':
                    manager = EdgeChromiumDriverManager()
                    service = EdgeService(manager.install())
                    option = webdriver.EdgeOptions()
                    # 设置浏览器不关闭
                    option.add_experimental_option('detach', True)
                    driver = webdriver.Edge(service=service, options=option)
                    end_time = time.time()
                    print("Edge驱动安装完成,"+"耗时:"+str(end_time-start_time)+"秒")
                case 'firefox':
                    manager = GeckoDriverManager()
                    service = FireFoxService(manager.install())
                    driver = webdriver.Firefox(service=service)
                    end_time = time.time()
                    print("Firefox驱动安装完成,"+"耗时:"+str(end_time-start_time)+"秒")
            return driver
        except Exception as e:
            print(f"驱动安装失败:{e}")
            return None
